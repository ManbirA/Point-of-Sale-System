# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

from .instance_configuration_instance_source_details import InstanceConfigurationInstanceSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InstanceConfigurationInstanceSourceViaBootVolumeDetails(InstanceConfigurationInstanceSourceDetails):
    """
    InstanceConfigurationInstanceSourceViaBootVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InstanceConfigurationInstanceSourceViaBootVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.InstanceConfigurationInstanceSourceViaBootVolumeDetails.source_type` attribute
        of this class is ``bootVolume`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        :type source_type: str

        :param boot_volume_id:
            The value to assign to the boot_volume_id property of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        :type boot_volume_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'boot_volume_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'boot_volume_id': 'bootVolumeId'
        }

        self._source_type = None
        self._boot_volume_id = None
        self._source_type = 'bootVolume'

    @property
    def boot_volume_id(self):
        """
        Gets the boot_volume_id of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        The OCID of the boot volume used to boot the instance.


        :return: The boot_volume_id of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        :rtype: str
        """
        return self._boot_volume_id

    @boot_volume_id.setter
    def boot_volume_id(self, boot_volume_id):
        """
        Sets the boot_volume_id of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        The OCID of the boot volume used to boot the instance.


        :param boot_volume_id: The boot_volume_id of this InstanceConfigurationInstanceSourceViaBootVolumeDetails.
        :type: str
        """
        self._boot_volume_id = boot_volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other