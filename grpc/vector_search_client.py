# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import grpc
import os

from . import vector_search_pb2
from . import vector_search_pb2_grpc


OD_HOST = os.environ['OD_HOST']
OD_PORT = os.environ['OD_PORT']


def run():
  channel = grpc.insecure_channel(OD_HOST + ':' + OD_PORT)
  stub = vector_search_pb2_grpc.SearchStub(channel)
  results = stub.SearchVector(vector_search_pb2.SearchRequest(vector=[0.99, 0.32]))

  for result in results:
    print(result)

if __name__ == '__main__':
  run()
