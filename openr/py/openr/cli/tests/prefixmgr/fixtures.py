#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-ignore-all-errors
from typing import Dict

from openr.KvStore import ttypes as openr_kvstore_types
from openr.Network.ttypes import BinaryAddress, IpPrefix
from openr.OpenrCtrl.ttypes import AdvertisedRoute, AdvertisedRouteDetail
from openr.Types.ttypes import PrefixEntry, PrefixMetrics

MOCKED_ADVERTISED_ROUTES = [
    AdvertisedRouteDetail(
        prefix=IpPrefix(
            prefixAddress=BinaryAddress(
                addr=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
            ),
            prefixLength=0,
        ),
        bestKey=3,
        bestKeys=[3],
        routes=[
            AdvertisedRoute(
                key=3,
                route=PrefixEntry(
                    prefix=IpPrefix(
                        prefixAddress=BinaryAddress(
                            addr=b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                        ),
                        prefixLength=0,
                    ),
                    type=3,
                    data=b"b''",
                    forwardingType=1,
                    forwardingAlgorithm=0,
                    minNexthop=24,
                    prependLabel=65001,
                    metrics=PrefixMetrics(
                        version=1,
                        path_preference=1000,
                        source_preference=100,
                        distance=4,
                    ),
                    tags={"65527:896", "65520:822", "65529:15990", "COMMODITY:EGRESS"},
                    area_stack=["64984", "65333", "64900", "65301"],
                ),
            )
        ],
    ),
    AdvertisedRouteDetail(
        prefix=IpPrefix(
            prefixAddress=BinaryAddress(addr=b"\x00\x00\x00\x00"), prefixLength=0
        ),
        bestKey=3,
        bestKeys=[3],
        routes=[
            AdvertisedRoute(
                key=3,
                route=PrefixEntry(
                    prefix=IpPrefix(
                        prefixAddress=BinaryAddress(addr=b"\x00\x00\x00\x00"),
                        prefixLength=0,
                    ),
                    type=3,
                    data=b"b''",
                    forwardingType=1,
                    forwardingAlgorithm=0,
                    minNexthop=24,
                    prependLabel=60000,
                    metrics=PrefixMetrics(
                        version=1,
                        path_preference=1000,
                        source_preference=100,
                        distance=4,
                    ),
                    tags={"65527:896", "65520:822", "65529:15990", "COMMODITY:EGRESS"},
                    area_stack=["64984", "65333", "64900", "65301"],
                ),
            )
        ],
    ),
]

ADVERTISED_ROUTES_OUTPUT = """\
Markers: * - Best entries (used for forwarding), @ - Entry used to advertise across area
Acronyms: SP - Source Preference, PP - Path Preference, D - Distance
          MN - Min-Nexthops, PL - Prepend Label

   Source                               FwdAlgo      FwdType  SP     PP     D      MN    PL    

> ::/0, 1/1
*@ BGP                                  SP_ECMP      SR_MPLS  100    1000   4      24    65001 

> 0.0.0.0/0, 1/1
*@ BGP                                  SP_ECMP      SR_MPLS  100    1000   4      24    60000 

"""

ADVERTISED_ROUTES_OUTPUT_DETAILED = """\
Markers: * - Best entries (used for forwarding), @ - Entry used to advertise across area

> ::/0, 1/1
*@ from BGP
     Forwarding - algorithm: SP_ECMP, type: SR_MPLS
     Metrics - path-preference: 1000, source-preference: 100, distance: 4, drained-path: 0
     Performance - min-nexthops: 24
     Misc - prepend-label: 65001, weight: None
     Tags - (NA)/65527:896, (NA)/65529:15990, (NA)/COMMODITY:EGRESS, TAG_NAME2/65520:822
     Area Stack - 64984, 65333, 64900, 65301

> 0.0.0.0/0, 1/1
*@ from BGP
     Forwarding - algorithm: SP_ECMP, type: SR_MPLS
     Metrics - path-preference: 1000, source-preference: 100, distance: 4, drained-path: 0
     Performance - min-nexthops: 24
     Misc - prepend-label: 60000, weight: None
     Tags - (NA)/65527:896, (NA)/65529:15990, (NA)/COMMODITY:EGRESS, TAG_NAME2/65520:822
     Area Stack - 64984, 65333, 64900, 65301

"""

# Keeping for reference
ADVERTISED_ROUTES_OUTPUT_JSON = """\
[
  {
    "bestKey": 3,
    "bestKeys": [
      3
    ],
    "prefix": "::/0",
    "routes": [
      {
        "hitPolicy": null,
        "igpCost": null,
        "key": 3,
        "route": {
          "area_stack": [
            "64984",
            "65333",
            "64900",
            "65301"
          ],
          "data": "b''",
          "forwardingAlgorithm": 0,
          "forwardingType": 1,
          "metrics": {
            "distance": 4,
            "drain_metric": 0,
            "path_preference": 1000,
            "source_preference": 100,
            "version": 1
          },
          "minNexthop": 24,
          "prefix": "::/0",
          "prependLabel": 65001,
          "tags": [
            "65520:822",
            "65527:896",
            "65529:15990",
            "COMMODITY:EGRESS"
          ],
          "type": 3,
          "weight": null
        }
      }
    ]
  },
  {
    "bestKey": 3,
    "bestKeys": [
      3
    ],
    "prefix": "0.0.0.0/0",
    "routes": [
      {
        "hitPolicy": null,
        "igpCost": null,
        "key": 3,
        "route": {
          "area_stack": [
            "64984",
            "65333",
            "64900",
            "65301"
          ],
          "data": "b''",
          "forwardingAlgorithm": 0,
          "forwardingType": 1,
          "metrics": {
            "distance": 4,
            "drain_metric": 0,
            "path_preference": 1000,
            "source_preference": 100,
            "version": 1
          },
          "minNexthop": 24,
          "prefix": "0.0.0.0/0",
          "prependLabel": 60000,
          "tags": [
            "65520:822",
            "65527:896",
            "65529:15990",
            "COMMODITY:EGRESS"
          ],
          "type": 3,
          "weight": null
        }
      }
    ]
  }
]
"""

MOCKED_INIT_EVENT_GOOD: Dict[openr_kvstore_types.InitializationEvent, int] = {
    openr_kvstore_types.InitializationEvent.PREFIX_DB_SYNCED: 9206,
}

MOCKED_INIT_EVENT_WARNING: Dict[openr_kvstore_types.InitializationEvent, int] = {
    openr_kvstore_types.InitializationEvent.PREFIX_DB_SYNCED: 170000,
}

MOCKED_INIT_EVENT_TIMEOUT: Dict[openr_kvstore_types.InitializationEvent, int] = {
    openr_kvstore_types.InitializationEvent.PREFIX_DB_SYNCED: 300000,
}
