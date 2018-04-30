.. _introduction:

Introduction
=============================

Purpose
-----------------------------

This document provides detailed metadata (data dictionary) for the simple and comprehensive NZ Building Outlines data published on the LINZ Data Service.

Background
----------------------------

Over the next decade, the LINZ Topographic Office is working towards its vision of recognising the way location information can help unlock new patterns and knowledge, particularly when it is combined with other types of information. One of our strategic goals is to improve national scale datasets and maximize their opportunities for reuse by a variety of national and regional stakeholders.

Building outlines have been identified as a dataset of national importance, and influence a multitude of decisions made across New Zealand at both the national and regional levels. It is therefore critical to have a consistent and dynamic dataset available. This building outline dataset will provide a foundation for various stakeholders to map risk modelling, environmental assessment, urban development, resilience planning in addition to the visualization and physical location of buildings. 

Description
---------------------------

This dataset includes the spatial coverage of buildings using remotely sensed information. A building outline is a digital representation of the roof outline of buildings which have been classified from remotely sensed information using a combination of automated and manual processes to extract and orthogonalise building roof outlines and identifies every structure greater than 9 square meters. These processes use electromagnetic radiation reflectance in the red, green and blue bands (visible bands) to classify pixels based on known patterns of signal combinations from various building roof materials.

File format
---------------------------

Aspatial data is provided in UTF-8 format. The source geometry of all spatial tables is NZGD2000 (New Zealand Geodetic Datum 2000).

Definitions
---------------------------

.. table::
   :widths: auto

   ========  ==============================================
     Term    Description
   ========  ==============================================
   Aspatial  Data that is not related to a spatial geometry
   LDS       LINZ Data Service
   ========  ==============================================

Data model and dictionary
---------------------------

To assist you in understanding these datasets, the structure and details of the data fields is described in tables below. The relationship between tables and directly related datasets is provided in a data model diagram. No attempt has been made to indicate cardinality, however, the arrows drawn between datasets point from the dataset containing the unique record, to the dataset that may contain one or more references to that record (i.e. primary key -> foreign key). 

To enable changes between updates to be recorded and then queried using the LDS changeset service, every table has a primary key. Primary keys are shown by a bolded and underlined field name. Tables can also have unique keys, which are shown by a bolded field name. 

This data model has been designed to manage building data with multiple representations, allowing for future enhancements in building data management. Not all of this data is currently available and data capture for these new fields will occur over time. Fields requiring data capture are shown in italics in the tables below.
