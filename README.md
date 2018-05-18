# Python library for iterating through CKAN packages

This package allows you to iterator through CKAN packages/datasets
Pythonically, with minimal code. It is released into the Public Domain.

## Requirements

ckanapi package

## Simple usage

```
from ckancrawler import Crawler

crawler = Crawler('https://data.humdata.org')

for package in crawler.packages(fq='tags:hxl'):
    print(package['name'])
```

## Crawler variables and methods

**ckan** - (variable) the underlying ckanapi object
_(Use this to perform operations on the data, per https://github.com/ckan/ckanapi)_

**__init__**(ckan_url='https://demo.ckan.org', apikey=None, user_agent=None, delay=1) - constructor

* ckan_url - the URL of the CKAN site to use (defaults to https://demo.ckan.org)
* apikey - your personal CKAN API key, for non-anonymous access
  (e.g. if you plan to make changes to packages or resources)
* user_agent - an HTTP user-agent string to pass to CKAN (usually not
  required)
* delay - delay in seconds between each result (to give the server a
  breath); defaults to 1
  
**packages**(query) - return a generator (iterator) through matching packages
* q - a CKAN search query (e.g. "education"); defaults to None (all packages)
* fq - a CKAN filter query (e.g. "tags:hxl"); defaults to None (all packages)
* sort - a CKAN sorting specification (e.g. "relevance asc, metadata_modified desc"); defaults to None
  (default sort)
  
## Sample CKAN package

The following is a sample package from the
[Humanitarian Data Exchange](https://data.humdata.org) (HDX), showing
typical fields available in a package/dataset object:


```
{
    "data_update_frequency": "0",
    "license_title": "cc-by-igo",
    "maintainer": "e043d6c9-890b-4fed-8dc1-d07ebb534733",
    "relationships_as_object": [],
    "private": false,
    "dataset_date": "01/01/1990-12/31/2027",
    "num_tags": 10,
    "solr_additions": "{\"countries\": [\"Syrian Arab Republic\"]}",
    "id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
    "metadata_created": "2015-12-03T20:23:34.557045",
    "caveats": "Live data from UNHCR (continuously updating).\n\nIn some recent data, figures between 1 and 4 have been replaced with an asterisk (*). These represent situations where the figures are being kept confidential to protect the anonymity of individuals. Such figures are not included in any totals.\n\nSome country data may be missing, where UNHCR adds extra text after the country name (e.g. \"France: all regions\").",
    "metadata_modified": "2017-10-24T21:30:26.980319",
    "author": null,
    "author_email": null,
    "subnational": "0",
    "state": "active",
    "has_geodata": false,
    "methodology": "Census",
    "version": null,
    "is_requestdata_type": false,
    "license_id": "cc-by-igo",
    "num_of_showcases": 2,
    "type": "dataset",
    "resources": [
        {
            "cache_last_updated": null,
            "package_id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
            "datastore_active": false,
            "id": "a125ca78-880b-4bcf-b368-70670f8ff49d",
            "size": null,
            "revision_last_updated": "2017-10-24T21:30:26.979086",
            "state": "active",
            "hash": "",
            "description": "UNHCR persons of concern originating from Syria.",
            "format": "CSV",
            "hdx_rel_url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/persons_of_concern.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "tracking_summary": {
                "total": 28,
                "recent": 1
            },
            "mimetype_inner": null,
            "url_type": null,
            "mimetype": "text/csv",
            "cache_url": null,
            "name": "unhcr_persons_of_concern_origin_syr.csv",
            "created": "2017-10-24T21:30:27.145690",
            "url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/persons_of_concern.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "last_modified": null,
            "position": 0,
            "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
            "resource_type": null
        },
        {
            "cache_last_updated": null,
            "package_id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
            "datastore_active": false,
            "id": "8e3c22b2-7038-40dc-bf1d-3ec2eaa3b0c9",
            "size": null,
            "revision_last_updated": "2017-10-24T21:30:26.979086",
            "state": "active",
            "hash": "",
            "description": "Time-series data for UNHCR persons of concern originating from Syria.",
            "format": "CSV",
            "hdx_rel_url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/time_series.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "tracking_summary": {
                "total": 17,
                "recent": 1
            },
            "mimetype_inner": null,
            "url_type": null,
            "mimetype": "text/csv",
            "cache_url": null,
            "name": "unhcr_time_series_origin_syr.csv",
            "created": "2017-10-24T21:30:27.145700",
            "url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/time_series.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "last_modified": null,
            "position": 1,
            "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
            "resource_type": null
        },
        {
            "cache_last_updated": null,
            "package_id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
            "datastore_active": false,
            "id": "1682cbdf-d863-4f10-9b6b-1d57f9d84437",
            "size": null,
            "revision_last_updated": "2017-10-24T21:30:26.979086",
            "state": "active",
            "hash": "",
            "description": "Demographic data for UNHCR persons of concern originating in Syria.",
            "format": "CSV",
            "hdx_rel_url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/demographics.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "tracking_summary": {
                "total": 19,
                "recent": 1
            },
            "mimetype_inner": null,
            "url_type": null,
            "mimetype": "text/csv",
            "cache_url": null,
            "name": "unhcr_demographics_origin_syr.csv",
            "created": "2017-10-24T21:30:27.145705",
            "url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/demographics.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "last_modified": null,
            "position": 2,
            "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
            "resource_type": null
        },
        {
            "cache_last_updated": null,
            "package_id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
            "datastore_active": false,
            "id": "a475822a-82f7-418a-9a20-7505ec2cb221",
            "size": null,
            "revision_last_updated": "2017-10-24T21:30:26.979086",
            "state": "active",
            "hash": "",
            "description": "Monthly numbers for refugees from Syria seeking asylum in other countries.",
            "format": "CSV",
            "hdx_rel_url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/asylum_seekers_monthly.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "tracking_summary": {
                "total": 19,
                "recent": 1
            },
            "mimetype_inner": null,
            "url_type": null,
            "mimetype": "text/csv",
            "cache_url": null,
            "name": "unhcr_asylum_seekers_monthly_origin_syr.csv",
            "created": "2017-10-24T21:30:27.145708",
            "url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/asylum_seekers_monthly.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "last_modified": null,
            "position": 3,
            "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
            "resource_type": null
        },
        {
            "cache_last_updated": null,
            "package_id": "e2d5566d-d755-40dd-a63f-d4d298a9df1d",
            "datastore_active": false,
            "id": "9d8d972d-22a9-46ae-b0b0-68956e861e89",
            "size": null,
            "revision_last_updated": "2017-10-24T21:30:26.979086",
            "state": "active",
            "hash": "",
            "description": "Refugees from Syria resettled in other countries.",
            "format": "CSV",
            "hdx_rel_url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/resettlement.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "tracking_summary": {
                "total": 10,
                "recent": 4
            },
            "mimetype_inner": null,
            "url_type": null,
            "mimetype": "text/csv",
            "cache_url": null,
            "name": "unhcr_resettlement_origin_syr.csv",
            "created": "2017-10-24T21:30:27.145712",
            "url": "http://proxy.hxlstandard.org/data.csv?url=http%3A//popstats.unhcr.org/en/resettlement.hxl&filter01=select&select-query01-01=%23country%2Borigin=Syrian%20Arab%20Rep.",
            "last_modified": null,
            "position": 4,
            "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
            "resource_type": null
        }
    ],
    "dataset_preview": "first_resource",
    "num_resources": 5,
    "dataset_source": "UNHCR",
    "tags": [
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "asylum-seekers",
            "id": "b927ab93-fac2-4628-a4f3-1fc12ce2cf14",
            "name": "asylum-seekers"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "hxl",
            "id": "5f985f56-ee63-40a7-9052-fd53269737ff",
            "name": "hxl"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "idp",
            "id": "9afc7d18-f686-4fd6-8013-aa48734eb83d",
            "name": "idp"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "idps",
            "id": "c8589b66-2b68-4fa4-992d-187e10696a8c",
            "name": "idps"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "internally displaced",
            "id": "85d7b638-36a0-4c35-97d4-9c9cbb23b3c5",
            "name": "internally displaced"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "protection",
            "id": "b131f272-0234-4194-8913-88f3c6f0b6b8",
            "name": "protection"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "refugee",
            "id": "5bb09d1f-4a0c-4425-90b9-dc9fe501f835",
            "name": "refugee"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "returned",
            "id": "8bf2358a-328a-482f-99ed-5bb7bcf4bfbf",
            "name": "returned"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "returned refugees",
            "id": "27e88d18-66f9-453f-9f0c-c6fb25ac527b",
            "name": "returned refugees"
        },
        {
            "vocabulary_id": null,
            "state": "active",
            "display_name": "stateless persons",
            "id": "1f95ca01-7852-4987-90dd-1175f213110b",
            "name": "stateless persons"
        }
    ],
    "revision_id": "56d37e04-7257-4aef-9bc7-7c4775f91664",
    "groups": [
        {
            "display_name": "Syrian Arab Republic",
            "description": "",
            "image_display_url": "",
            "title": "Syrian Arab Republic",
            "id": "syr",
            "name": "syr"
        }
    ],
    "creator_user_id": "7ae95211-71dd-484e-8538-2c625315eb56",
    "has_quickcharts": false,
    "maintainer_email": null,
    "relationships_as_subject": [],
    "total_res_downloads": 174,
    "organization": {
        "description": "The Office of the United Nations High Commissioner for Refugees was established on December 14, 1950 by the United Nations General Assembly. The agency is mandated to lead and co-ordinate international action to protect refugees and resolve refugee problems worldwide. Its primary purpose is to safeguard the rights and well-being of refugees. It strives to ensure that everyone can exercise the right to seek asylum and find safe refuge in another State, with the option to return home voluntarily, integrate locally or to resettle in a third country. It also has a mandate to help stateless people.",
        "created": "2014-05-21T12:08:06.445758",
        "title": "UNHCR - The UN Refugee Agency",
        "name": "unhcr",
        "is_organization": true,
        "state": "active",
        "image_url": "",
        "revision_id": "313ec3fa-0f55-43ec-8b66-eb9ff098b631",
        "type": "organization",
        "id": "abf4ca86-8e69-40b1-92f7-71509992be88",
        "approval_status": "approved"
    },
    "name": "refugees-originating-syr",
    "isopen": false,
    "url": null,
    "notes": "Data about UNHCR's populations of concern originating from Syria. There are five types of data available (by year, unless otherwise noted): \n\n1. Persons of concern\n\n2. Time-series data for refugees\n\n3. Refugee status determination for asylum seekers\n\n4. Number of asylum seekers (by month).\n\n5. Refugees resettled.\n\nThe source data comes from the [UNHCR Population Statistics](http://popstats.unhcr.org/en/overview) portal.",
    "owner_org": "abf4ca86-8e69-40b1-92f7-71509992be88",
    "has_showcases": true,
    "pageviews_last_14_days": 9,
    "title": "UNHCR's populations of concern originating from Syria",
    "package_creator": "davidmegginson"
}
```
