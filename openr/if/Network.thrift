/**
 * Copyright (c) 2014-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

namespace cpp2 openr.thrift
namespace py openr.Network
namespace php Openr

# fbstring uses the small internal buffer to store the data
# if the data is small enough (< 24 bytes).
typedef binary (cpp.type = "::folly::fbstring") fbbinary

// Using the defaults from here:
// https://en.wikipedia.org/wiki/Administrative_distance
enum AdminDistance {
  DIRECTLY_CONNECTED = 0,
  STATIC_ROUTE = 1,
  EBGP = 20,
  IBGP = 200,
  NETLINK_LISTENER = 225,
  MAX_ADMIN_DISTANCE = 255
}

struct BinaryAddress {
  1: required fbbinary addr
  3: optional string ifName
}

struct IpPrefix {
  1: BinaryAddress prefixAddress
  2: i16 prefixLength
}

struct NextHopThrift {
  1: BinaryAddress address
  // Default weight of 0 represents an ECMP route.
  // This default is chosen for two reasons:
  // 1) We rely on the arithmetic properties of 0 for ECMP vs UCMP route
  //    resolution calculations. A 0 weight next hop being present at a variety
  //    of layers in a route resolution tree will cause the entire route
  //    resolution to use ECMP.
  // 2) A client which does not set a value will result in
  //    0 being populated even with strange behavior in the client language
  //    which is consistent with C++
  2: i32 weight = 0
}

struct UnicastRoute {
  1: required IpPrefix dest
  2: list<BinaryAddress> nexthops
  3: optional AdminDistance adminDistance
  4: list<NextHopThrift> nextHops
}
