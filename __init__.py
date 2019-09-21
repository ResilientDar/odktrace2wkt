# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ODKTrace2WKT
                                 A QGIS plugin
 This plugin converts ODK geotraces to Well-Known Text
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-09-07
        copyright            : (C) 2019 by Samweli Mwakisambwe
        email                : smwltwesa6@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ODKTrace2WKT class from file ODKTrace2WKT.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .odktrace2wkt import ODKTrace2WKT
    return ODKTrace2WKT(iface)
