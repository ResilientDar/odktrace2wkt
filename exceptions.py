# -*- coding: utf-8 -*-
"""
/***************************************************************************
 exception classes
                                 A QGIS plugin
 This plugin create ODKTrace2WKT maps.
                             -------------------
        begin                : 2019-09-07
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Samweli Mwakisambwe
        email                : smwakisambwe@worldbank.org
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


class ODKTrace2WKTError(RuntimeError):
    """Base class for all user defined exceptions"""
    suggestion = 'An unspecified error occurred.'


class ReadLayerError(ODKTrace2WKTError):
    """When a layer can't be read"""
    suggestion = (
        'Check that the file exists and you have permissions to read it')


class WriteLayerError(ODKTrace2WKTError):
    """When a layer can't be written"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class BoundingBoxError(ODKTrace2WKTError):
    """For errors relating to bboxes"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class VerificationError(ODKTrace2WKTError):
    """Exception thrown by verify()
    """
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class PolygonInputError(ODKTrace2WKTError):
    """For invalid inputs to numeric polygon functions"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class PointsInputError(ODKTrace2WKTError):
    """For invalid inputs to numeric point functions"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class BoundsError(ODKTrace2WKTError):
    """For points falling outside interpolation grid"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class GetDataError(ODKTrace2WKTError):
    """When layer data cannot be obtained"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class PostProcessorError(ODKTrace2WKTError):
    """Raised when requested import cannot be performed if QGIS is too old."""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class WindowsError(ODKTrace2WKTError):
    """For windows specific errors."""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class GridXmlFileNotFoundError(ODKTrace2WKTError):
    """An exception for when an grid.xml could not be found"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class GridXmlParseError(ODKTrace2WKTError):
    """An exception for when something went wrong parsing the grid.xml """
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class ContourCreationError(ODKTrace2WKTError):
    """An exception for when creating contours from shakemaps goes wrong"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class InvalidLayerError(ODKTrace2WKTError):
    """Raised when a gis layer is invalid"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class ShapefileCreationError(ODKTrace2WKTError):
    """Raised if an error occurs creating the cities file"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class ZeroImpactException(ODKTrace2WKTError):
    """Raised if an impact function return zero impact"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class WrongDataTypeException(ODKTrace2WKTError):
    """Raised if expected and received data types are different"""
    suggestion = 'Please ask the developers of ODKTrace2WKT to add a suggestion.'


class InvalidClipGeometryError(ODKTrace2WKTError):
    """Custom exception for when clip geometry is invalid."""
    pass


class FileNotFoundError(ODKTrace2WKTError):
    """Custom exception for when a file could not be found."""
    pass


class TestNotImplementedError(ODKTrace2WKTError):
    """Custom exception for when a test exists only as a stub."""
    pass


class NoFunctionsFoundError(ODKTrace2WKTError):
    """Custom exception for when a no impact calculation
    functions can be found."""
    pass


class KeywordDbError(ODKTrace2WKTError):
    """Custom exception for when an error is encountered with keyword cache db.
    """
    pass


class HashNotFoundError(ODKTrace2WKTError):
    """Custom exception for when a no keyword hash can be found."""
    pass


class StyleInfoNotFoundError(ODKTrace2WKTError):
    """Custom exception for when a no styleInfo can be found."""
    pass


class InvalidParameterError(ODKTrace2WKTError):
    """Custom exception for when an invalid parameter is passed to a function.
    """
    pass


class TranslationLoadError(ODKTrace2WKTError):
    """Custom exception handler for whe translation file fails
    to load."""
    pass


class LegendLayerError(ODKTrace2WKTError):
    """An exception raised when trying to create a legend from
    a QgsMapLayer that does not have suitable characteristics to
    allow a legend to be created from it."""
    pass


class NoFeaturesInExtentError(ODKTrace2WKTError):
    """An exception that gets thrown when no features are within
    the extent being clipped."""
    pass


class InvalidProjectionError(ODKTrace2WKTError):
    """An exception raised if a layer needs to be reprojected."""
    pass


class InsufficientOverlapError(ODKTrace2WKTError):
    """An exception raised if an error occurs during extent calculation
    because the bounding boxes do not overlap."""
    pass


class StyleError(ODKTrace2WKTError):
    """An exception relating to reading / generating GIS styles"""
    pass


class MemoryLayerCreationError(ODKTrace2WKTError):
    """Raised if an error occurs creating the cities file"""
    pass


class MethodUnavailableError(ODKTrace2WKTError):
    """Raised if the requested import cannot be performed dur to qgis being
    to old"""
    pass


class CallGDALError(ODKTrace2WKTError):
    """Raised if failed to call gdal command. Indicate by error message that is
    not empty"""
    pass


class ImportDialogError(ODKTrace2WKTError):
    """Raised if import process failed."""
    pass


class FileMissingError(ODKTrace2WKTError):
    """Raised if a file cannot be found."""
    pass


class CanceledImportDialogError(ODKTrace2WKTError):
    """Raised if import process canceled"""
    pass


class HelpFileMissingError(ODKTrace2WKTError):
    """Raised if a help file cannot be found."""
    pass


class InvalidGeometryError(ODKTrace2WKTError):
    """Custom exception for when a feature geometry is invalid or none."""
    pass


class UnsupportedProviderError(ODKTrace2WKTError):
    """For unsupported provider (e.g. openlayers plugin) encountered."""
    pass


class ReportCreationError(ODKTrace2WKTError):
    """Raised when error occurs during report generation."""
    pass


class EmptyDirectoryError(ODKTrace2WKTError):
    """Raised when output directory is empty string path."""
    pass


class NoValidLayerError(ODKTrace2WKTError):
    """Raised when there no valid layer in ODKTrace2WKT."""
    pass


class InsufficientMemoryWarning(ODKTrace2WKTError):
    """Raised when there is a possible insufficient memory."""
    pass


class InvalidExtentError(ODKTrace2WKTError):
    """Raised if an extent is not valid."""
    pass


class NoAttributeInLayerError(ODKTrace2WKTError):
    """Raised if the attribute not exists in the vector layer"""
    pass
