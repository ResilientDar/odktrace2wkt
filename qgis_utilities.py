# -*- coding: utf-8 -*-
"""
/***************************************************************************
                                 A QGIS plugin
 This plugin converts geotraces to wkt.
                             -------------------
        begin                : 2019-09-07
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Samweli Mwakisambwe
        email                : smwltwesa6@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from qgis.PyQt.QtWidgets import QMessageBox
from datetime import date
from tempfile import mkstemp

import sys
import os
import getpass

QGIS_APP = None
CANVAS = None
PARENT = None
IFACE = None


def display_information_message_box(
        parent=None, title=None, message=None):
    """
    Display an information message box.

    :param title: The title of the message box.
    :type title: str

    :param message: The message inside the message box.
    :type message: str
    """
    QMessageBox.information(parent, title, message)


def display_warning_message_box(parent=None, title=None, message=None):
    """
    Display a warning message box.

    :param title: The title of the message box.
    :type title: str

    :param message: The message inside the message box.
    :type message: str
    """
    QMessageBox.warning(parent, title, message)


def display_critical_message_box(parent=None, title=None, message=None):
    """
    Display a critical message box.

    :param title: The title of the message box.
    :type title: str

    :param message: The message inside the message box.
    :type message: str
    """
    QMessageBox.critical(parent, title, message)


def get_qgis_app():
    """ Start one QGIS application to test against.

    :returns: Handle to QGIS app, canvas, iface and parent. If there are any
        errors the tuple members will be returned as None.
    :rtype: (QgsApplication, CANVAS, IFload_standard_layersACE, PARENT)

    If QGIS is already running the handle to that app will be returned.
    """

    try:
        from qgis.core import QgsApplication
        from qgis.gui import QgsMapCanvas  # pylint: disable=no-name-in-module
        # noinspection PyPackageRequirements
        from qgis.PyQt import QtGui, QtCore  # pylint: disable=W0621
        # noinspection PyPackageRequirements
        from qgis.PyQt.QtCore import QCoreApplication, QSettings
        from qgis.gui import QgisInterface
    except ImportError:
        return None, None, None, None

    global QGIS_APP  # pylint: disable=W0603

    if QGIS_APP is None:
        gui_flag = True  # All test will run qgis in gui mode

        # AG: For testing purposes, we use our own configuration file instead
        # of using the QGIS apps conf of the host
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setOrganizationName('QGIS')
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setOrganizationDomain('qgis.org')
        # noinspection PyCallByClass,PyArgumentList
        QCoreApplication.setApplicationName('IsochronesTesting')

        # noinspection PyPep8Naming
        QGIS_APP = QgsApplication(sys.argv, gui_flag)

        # Make sure QGIS_PREFIX_PATH is set in your env if needed!
        QGIS_APP.initQgis()
        s = QGIS_APP.showSettings()

        # Save some settings
        settings = QSettings()
        settings.setValue('locale/overrideFlag', True)
        settings.setValue('locale/userLocale', 'en_US')
        # We disabled message bars for now for extent selector as
        # we don't have a main window to show them in TS - version 3.2

    global PARENT  # pylint: disable=W0603
    if PARENT is None:
        # noinspection PyPep8Naming
        PARENT = QtGui.QWidget()

    global CANVAS  # pylint: disable=W0603
    if CANVAS is None:
        # noinspection PyPep8Naming
        CANVAS = QgsMapCanvas(PARENT)
        CANVAS.resize(QtCore.QSize(400, 400))

    global IFACE  # pylint: disable=W0603
    if IFACE is None:
        # QgisInterface is a stub implementation of the QGIS plugin interface
        # noinspection PyPep8Naming
        IFACE = QgisInterface(CANVAS)

    return QGIS_APP, CANVAS, IFACE, PARENT


def temp_dir(sub_dir='work'):
    """Obtain the temporary working directory for the operating system.
    A subdirectory will automatically be created under this and
    if specified, a user subdirectory under that.
    .. note:: You can use this together with unique_filename to create
       a file in a temporary directory under the odktrace2wkt workspace. e.g.
       tmpdir = temp_dir('testing')
       tmpfile = unique_filename(dir=tmpdir)
       print tmpfile
       /tmp/odktrace2wkt/02-01-2019/username/testing/tmpMRpF_C
    If you specify ODKTRACE2WKT_WORK_DIR as an environment var, it will be
    used in preference to the system temp directory.
    :param sub_dir: Optional argument which will cause an additional
        subdirectory to be created e.g. /tmp/odktrace2wkt/foo/
    :type sub_dir: str
    :return: Path to the temp dir that is created.
    :rtype: str
    :raises: Any errors from the underlying system calls.
    """
    user = getpass.getuser().replace(' ', '_')
    current_date = date.today()
    date_string = current_date.isoformat()
    if 'ODKTRACE2WKT_WORK_DIR' in os.environ:
        new_directory = os.environ['ODKTRACE2WKT_WORK_DIR']
    else:
        # Following 4 lines are a workaround for tempfile.tempdir()
        # unreliabilty
        handle, filename = mkstemp()
        os.close(handle)
        new_directory = os.path.dirname(filename)
        os.remove(filename)

    path = os.path.join(
        new_directory,
        'odktrace2wkt',
        date_string,
        user,
        sub_dir
        )

    if not os.path.exists(path):
        # Ensure that the dir is world writable
        # Umask sets the new mask and returns the old
        old_mask = os.umask(0000)
        os.makedirs(path, 0o777)
        # Reinstate the old mask for tmp
        os.umask(old_mask)
    return path


def unique_filename(**kwargs):
    """Create new filename guaranteed not to exist previously
    Use mkstemp to create the file, then remove it and return the name
    If dir is specified, the tempfile will be created in the path specified
    otherwise the file will be created in a directory following this scheme:
    :file:'/tmp/odktrace2wkt/<dd-mm-yyyy>/<user>/impacts'
    See http://docs.python.org/library/tempfile.html for details.
    Example usage:
    tempdir = temp_dir(sub_dir='test')
    filename = unique_filename(suffix='.foo', dir=tempdir)
    print filename
    /tmp/odktrace2wkt/02-03-2019/username/test/tmpyeO5VR.foo
    Or with no preferred subdir, a default subdir of 'files' is used:
    filename = unique_filename(suffix='.shp')
    print filename
     /tmp/odktrace2wkt/02-03-2019/username/files/tmpoOAmOi.shp
    """
    if 'dir' not in kwargs:
        path = temp_dir('files')
        kwargs['dir'] = path
    else:
        path = temp_dir(kwargs['dir'])
        kwargs['dir'] = path
    if not os.path.exists(kwargs['dir']):
        # Ensure that the dir mask won't conflict with the mode
        # Umask sets the new mask and returns the old
        umask = os.umask(0000)
        # Ensure that the dir is world writable by explicitly setting mode
        os.makedirs(kwargs['dir'], 0o777)
        # Reinstate the old mask for tmp dir
        os.umask(umask)
    # Now we have the working dir set up go on and return the filename
    handle, filename = mkstemp(**kwargs)

    # Need to close it using the file handle first for windows!
    os.close(handle)
    try:
        os.remove(filename)
    except OSError:
        pass
    return filename


def enable_busy_cursor():
    """Set the hourglass enabled and stop listening for layer changes."""

    from qgis.core import QgsApplication
    from qgis.PyQt import QtGui, QtCore

    QgsApplication.instance().setOverrideCursor(
        QtGui.QCursor(QtCore.Qt.WaitCursor)
    )


def disable_busy_cursor():
    """Disable the hourglass cursor and listen for layer changes."""

    from qgis.core import QgsApplication
    from qgis.PyQt import QtCore

    while QgsApplication.instance().overrideCursor() is not None and \
            QgsApplication.instance().overrideCursor().shape() == \
            QtCore.Qt.WaitCursor:
        QgsApplication.instance().restoreOverrideCursor()
