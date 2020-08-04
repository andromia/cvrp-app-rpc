# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from app import util
from app.api.models.base_model_ import Model
from app.api.v0_1.models.demand import Demand  # noqa: F401,E501
from app.api.v0_1.models.latitude import Latitude  # noqa: F401,E501
from app.api.v0_1.models.longitude import Longitude  # noqa: F401,E501
from app.api.v0_1.models.quantity import Quantity  # noqa: F401,E501


class Solution(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        latitude: Latitude = None,
        longitude: Longitude = None,
        quantity: Quantity = None,
        cluster_id: int = None,
        vehicle_id: int = None,
        stop_num: int = None,
    ):  # noqa: E501
        """Solution - a model defined in Swagger

        :param latitude: The latitude of this Solution.  # noqa: E501
        :type latitude: Latitude
        :param longitude: The longitude of this Solution.  # noqa: E501
        :type longitude: Longitude
        :param quantity: The quantity of this Solution.  # noqa: E501
        :type quantity: Quantity
        :param cluster_id: The cluster_id of this Solution.  # noqa: E501
        :type cluster_id: int
        :param vehicle_id: The vehicle_id of this Solution.  # noqa: E501
        :type vehicle_id: int
        :param stop_num: The stop_num of this Solution.  # noqa: E501
        :type stop_num: int
        """
        self.swagger_types = {
            "latitude": Latitude,
            "longitude": Longitude,
            "quantity": Quantity,
            "cluster_id": int,
            "vehicle_id": int,
            "stop_num": int,
        }

        self.attribute_map = {
            "latitude": "latitude",
            "longitude": "longitude",
            "quantity": "quantity",
            "cluster_id": "cluster_id",
            "vehicle_id": "vehicle_id",
            "stop_num": "stop_num",
        }
        self._latitude = latitude
        self._longitude = longitude
        self._quantity = quantity
        self._cluster_id = cluster_id
        self._vehicle_id = vehicle_id
        self._stop_num = stop_num

    @classmethod
    def from_dict(cls, dikt) -> "Solution":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Solution of this Solution.  # noqa: E501
        :rtype: Solution
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latitude(self) -> Latitude:
        """Gets the latitude of this Solution.


        :return: The latitude of this Solution.
        :rtype: Latitude
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: Latitude):
        """Sets the latitude of this Solution.


        :param latitude: The latitude of this Solution.
        :type latitude: Latitude
        """

        self._latitude = latitude

    @property
    def longitude(self) -> Longitude:
        """Gets the longitude of this Solution.


        :return: The longitude of this Solution.
        :rtype: Longitude
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: Longitude):
        """Sets the longitude of this Solution.


        :param longitude: The longitude of this Solution.
        :type longitude: Longitude
        """

        self._longitude = longitude

    @property
    def quantity(self) -> Quantity:
        """Gets the quantity of this Solution.


        :return: The quantity of this Solution.
        :rtype: Quantity
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: Quantity):
        """Sets the quantity of this Solution.


        :param quantity: The quantity of this Solution.
        :type quantity: Quantity
        """

        self._quantity = quantity

    @property
    def cluster_id(self) -> int:
        """Gets the cluster_id of this Solution.


        :return: The cluster_id of this Solution.
        :rtype: int
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id: int):
        """Sets the cluster_id of this Solution.


        :param cluster_id: The cluster_id of this Solution.
        :type cluster_id: int
        """

        self._cluster_id = cluster_id

    @property
    def vehicle_id(self) -> int:
        """Gets the vehicle_id of this Solution.


        :return: The vehicle_id of this Solution.
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id: int):
        """Sets the vehicle_id of this Solution.


        :param vehicle_id: The vehicle_id of this Solution.
        :type vehicle_id: int
        """

        self._vehicle_id = vehicle_id

    @property
    def stop_num(self) -> int:
        """Gets the stop_num of this Solution.


        :return: The stop_num of this Solution.
        :rtype: int
        """
        return self._stop_num

    @stop_num.setter
    def stop_num(self, stop_num: int):
        """Sets the stop_num of this Solution.


        :param stop_num: The stop_num of this Solution.
        :type stop_num: int
        """

        self._stop_num = stop_num