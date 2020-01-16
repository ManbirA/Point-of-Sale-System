# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PeerRegionForRemotePeering(object):
    """
    Details about a region that supports remote VCN peering. For more information, see `VCN Peering`__.

    __ https://docs.cloud.oracle.com/Content/Network/Tasks/VCNpeering.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PeerRegionForRemotePeering object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this PeerRegionForRemotePeering.
        :type name: str

        """
        self.swagger_types = {
            'name': 'str'
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this PeerRegionForRemotePeering.
        The region's name.

        Example: `us-phoenix-1`


        :return: The name of this PeerRegionForRemotePeering.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PeerRegionForRemotePeering.
        The region's name.

        Example: `us-phoenix-1`


        :param name: The name of this PeerRegionForRemotePeering.
        :type: str
        """
        self._name = name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
