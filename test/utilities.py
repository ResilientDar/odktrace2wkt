# coding=utf-8
"""Common functionality used by regression tests."""

import sys
import logging
import os
from tempfile import mkdtemp

from qgis.core import (
    QgsCoordinateReferenceSystem,
    QgsProject,
    QgsRasterLayer,
    QgsRectangle,
    QgsVectorLayer
)
from qgis.PyQt import QtWidgets
from qgis.PyQt.QtCore import QTranslator
import sip
from qgis.utils import iface
from collections import OrderedDict
from qgis.PyQt.QtCore import QSettings

LOGGER = logging.getLogger('QGIS')
QGIS_APP = None  # Static variable used to hold hand to running QGIS app
CANVAS = None
PARENT = None
IFACE = None


def qgis_iface():
    """Helper method to get the iface for testing.
    :return: The QGIS interface.
    :rtype: QgsInterface
    """
    from qgis.utils import iface
    if iface is not None:
        return iface
    else:
        from qgis.testing.mocked import get_iface
        return get_iface()


def get_qgis_app(requested_locale='en_US', qsetting=''):
    """ Start one QGIS application to test against.
    :param locale: The locale we want the qgis to launch with.
    :type locale: str
    :param qsetting: String to specify the QSettings. By default,
        use empty string.
    :type qsetting: str
    :returns: Handle to QGIS app, canvas, iface and parent. If there are any
        errors the tuple members will be returned as None.
    :rtype: (QgsApplication, CANVAS, IFACE, PARENT)
    If QGIS is already running the handle to that app will be returned.
    """
    global QGIS_APP, PARENT, IFACE, CANVAS  # pylint: disable=W0603

    from qgis.PyQt.QtCore import QSettings
    if qsetting:
        settings = QSettings(qsetting)
    else:
        settings = QSettings()

    try:
        current_locale = settings.value(
            'locale/userLocale',
            'en_US')
    except TypeError as e:
        pass

    locale_match = current_locale == requested_locale

    if iface and locale_match:
        from qgis.core import QgsApplication
        QGIS_APP = QgsApplication
        CANVAS = iface.mapCanvas()
        PARENT = iface.mainWindow()
        IFACE = iface

    try:
        from qgis.core import QgsApplication
        from qgis.gui import QgsMapCanvas  # pylint: disable=no-name-in-module
        # noinspection PyPackageRequirements
        from qgis.PyQt import QtWidgets, QtCore  # pylint: disable=W0621
        # noinspection PyPackageRequirements
        from qgis.PyQt.QtCore import QCoreApplication, QSettings
    except ImportError:
        return None, None, None, None

    if not QGIS_APP:
        gui_flag = True  # All test will run qgis in gui mode

        # AG: For testing purposes, we use our own configuration file
        # instead of using the QGIS apps conf of the host
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setOrganizationName('QGIS')
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setOrganizationDomain('qgis.org')
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setApplicationName('QGIS3Testing')

        # noinspection PyPep8Naming
        if 'argv' in dir(sys):
            QGIS_APP = QgsApplication([p.encode('utf-8')
                                       for p in sys.argv], gui_flag)
        else:
            QGIS_APP = QgsApplication([], gui_flag)

        # Make sure QGIS_PREFIX_PATH is set in your env if needed!
        QGIS_APP.initQgis()

        s = QGIS_APP.showSettings()
        LOGGER.debug(s)

    if not locale_match:
        """Setup internationalisation for the plugin."""

        if not settings:
            settings = QSettings()

        settings.setValue('locale/userLocale',
                           deep_convert_dict(
                               requested_locale))

        locale_name = str(requested_locale).split('_')[0]
        os.environ['LANG'] = str(locale_name)

        i18n_path = os.path.join(
        os.path.dirname(__file__), '../')

        i18n_path = os.path.join(i18n_path, 'i18n')

        translation_path = os.path.join(
            i18n_path, '_' + str(locale_name) + '.qm')

        if os.path.exists(translation_path):
            if isinstance(QGIS_APP, sip.wrappertype):
                translator = QTranslator()
            else:
                translator = QTranslator(QGIS_APP)
            result = translator.load(translation_path)
            if not result:
                message = 'Failed to load translation for %s' % locale_name
                raise Exception(message)
            # noinspection PyTypeChecker,PyCallByClass
            QCoreApplication.installTranslator(translator)

    if PARENT is None:
        # noinspection PyPep8Naming
        PARENT = QtWidgets.QWidget()

    if CANVAS is None:
        # noinspection PyPep8Naming
        CANVAS = QgsMapCanvas(PARENT)
        CANVAS.resize(QtCore.QSize(400, 400))

    return QGIS_APP, CANVAS, IFACE, PARENT


def deep_convert_dict(value):
    """Converts any OrderedDict elements in a value to
    ordinary dictionaries, safe for storage in QSettings
    :param value: value to convert
    :type value: Union[dict,OrderedDict]
    :return: dict
    """
    to_ret = value
    if isinstance(value, OrderedDict):
        to_ret = dict(value)

    try:
        for k, v in to_ret.items():
            to_ret[k] = deep_convert_dict(v)
    except AttributeError:
        pass

    return to_ret