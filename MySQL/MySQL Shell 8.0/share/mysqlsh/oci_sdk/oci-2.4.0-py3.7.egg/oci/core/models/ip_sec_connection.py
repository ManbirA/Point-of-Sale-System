# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IPSecConnection(object):
    """
    A connection between a DRG and CPE. This connection consists of multiple IPSec
    tunnels. Creating this connection is one of the steps required when setting up
    an IPSec VPN.

    **Important:**  Each tunnel in an IPSec connection can use either static routing or BGP dynamic
    routing (see the :class:`IPSecConnectionTunnel` object's
    `routing` attribute). Originally only static routing was supported and
    every IPSec connection was required to have at least one static route configured.
    To maintain backward compatibility in the API when support for BPG dynamic routing was introduced,
    the API accepts an empty list of static routes if you configure both of the IPSec tunnels to use
    BGP dynamic routing. If you switch a tunnel's routing from `BGP` to `STATIC`, you must first
    ensure that the IPSec connection is configured with at least one valid CIDR block static route.
    Oracle uses the IPSec connection's static routes when routing a tunnel's traffic *only*
    if that tunnel's `routing` attribute = `STATIC`. Otherwise the static routes are ignored.

    For more information about the workflow for setting up an IPSec connection, see
    `IPSec VPN`__.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized,
    talk to an administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    **Warning:** Oracle recommends that you avoid using any confidential information when you
    supply string values using the API.

    __ https://docs.cloud.oracle.com/Content/Network/Tasks/managingIPsec.htm
    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a IPSecConnection.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnection.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnection.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a IPSecConnection.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the cpe_local_identifier_type property of a IPSecConnection.
    #: This constant has a value of "IP_ADDRESS"
    CPE_LOCAL_IDENTIFIER_TYPE_IP_ADDRESS = "IP_ADDRESS"

    #: A constant which can be used with the cpe_local_identifier_type property of a IPSecConnection.
    #: This constant has a value of "HOSTNAME"
    CPE_LOCAL_IDENTIFIER_TYPE_HOSTNAME = "HOSTNAME"

    def __init__(self, **kwargs):
        """
        Initializes a new IPSecConnection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this IPSecConnection.
        :type compartment_id: str

        :param cpe_id:
            The value to assign to the cpe_id property of this IPSecConnection.
        :type cpe_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this IPSecConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this IPSecConnection.
        :type display_name: str

        :param drg_id:
            The value to assign to the drg_id property of this IPSecConnection.
        :type drg_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IPSecConnection.
        :type freeform_tags: dict(str, str)

        :param id:
            The value to assign to the id property of this IPSecConnection.
        :type id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IPSecConnection.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param cpe_local_identifier:
            The value to assign to the cpe_local_identifier property of this IPSecConnection.
        :type cpe_local_identifier: str

        :param cpe_local_identifier_type:
            The value to assign to the cpe_local_identifier_type property of this IPSecConnection.
            Allowed values for this property are: "IP_ADDRESS", "HOSTNAME", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type cpe_local_identifier_type: str

        :param static_routes:
            The value to assign to the static_routes property of this IPSecConnection.
        :type static_routes: list[str]

        :param time_created:
            The value to assign to the time_created property of this IPSecConnection.
        :type time_created: datetime

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'cpe_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'drg_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'id': 'str',
            'lifecycle_state': 'str',
            'cpe_local_identifier': 'str',
            'cpe_local_identifier_type': 'str',
            'static_routes': 'list[str]',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'cpe_id': 'cpeId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'drg_id': 'drgId',
            'freeform_tags': 'freeformTags',
            'id': 'id',
            'lifecycle_state': 'lifecycleState',
            'cpe_local_identifier': 'cpeLocalIdentifier',
            'cpe_local_identifier_type': 'cpeLocalIdentifierType',
            'static_routes': 'staticRoutes',
            'time_created': 'timeCreated'
        }

        self._compartment_id = None
        self._cpe_id = None
        self._defined_tags = None
        self._display_name = None
        self._drg_id = None
        self._freeform_tags = None
        self._id = None
        self._lifecycle_state = None
        self._cpe_local_identifier = None
        self._cpe_local_identifier_type = None
        self._static_routes = None
        self._time_created = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPSec connection.


        :return: The compartment_id of this IPSecConnection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IPSecConnection.
        The OCID of the compartment containing the IPSec connection.


        :param compartment_id: The compartment_id of this IPSecConnection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def cpe_id(self):
        """
        **[Required]** Gets the cpe_id of this IPSecConnection.
        The OCID of the :class:`Cpe` object.


        :return: The cpe_id of this IPSecConnection.
        :rtype: str
        """
        return self._cpe_id

    @cpe_id.setter
    def cpe_id(self, cpe_id):
        """
        Sets the cpe_id of this IPSecConnection.
        The OCID of the :class:`Cpe` object.


        :param cpe_id: The cpe_id of this IPSecConnection.
        :type: str
        """
        self._cpe_id = cpe_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IPSecConnection.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this IPSecConnection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IPSecConnection.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this IPSecConnection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this IPSecConnection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this IPSecConnection.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this IPSecConnection.
        :type: str
        """
        self._display_name = display_name

    @property
    def drg_id(self):
        """
        **[Required]** Gets the drg_id of this IPSecConnection.
        The OCID of the DRG.


        :return: The drg_id of this IPSecConnection.
        :rtype: str
        """
        return self._drg_id

    @drg_id.setter
    def drg_id(self, drg_id):
        """
        Sets the drg_id of this IPSecConnection.
        The OCID of the DRG.


        :param drg_id: The drg_id of this IPSecConnection.
        :type: str
        """
        self._drg_id = drg_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IPSecConnection.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this IPSecConnection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IPSecConnection.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this IPSecConnection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def id(self):
        """
        **[Required]** Gets the id of this IPSecConnection.
        The IPSec connection's Oracle ID (OCID).


        :return: The id of this IPSecConnection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IPSecConnection.
        The IPSec connection's Oracle ID (OCID).


        :param id: The id of this IPSecConnection.
        :type: str
        """
        self._id = id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this IPSecConnection.
        The IPSec connection's current state.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IPSecConnection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IPSecConnection.
        The IPSec connection's current state.


        :param lifecycle_state: The lifecycle_state of this IPSecConnection.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def cpe_local_identifier(self):
        """
        Gets the cpe_local_identifier of this IPSecConnection.
        Your identifier for your CPE device. Can be either an IP address or a hostname (specifically,
        the fully qualified domain name (FQDN)). The type of identifier here must correspond
        to the value for `cpeLocalIdentifierType`.

        If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute
        for the :class:`Cpe` object specified by `cpeId` is used as the `cpeLocalIdentifier`.

        For information about why you'd provide this value, see
        `If Your CPE Is Behind a NAT Device`__.

        Example IP address: `10.0.3.3`

        Example hostname: `cpe.example.com`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/overviewIPsec.htm#nat


        :return: The cpe_local_identifier of this IPSecConnection.
        :rtype: str
        """
        return self._cpe_local_identifier

    @cpe_local_identifier.setter
    def cpe_local_identifier(self, cpe_local_identifier):
        """
        Sets the cpe_local_identifier of this IPSecConnection.
        Your identifier for your CPE device. Can be either an IP address or a hostname (specifically,
        the fully qualified domain name (FQDN)). The type of identifier here must correspond
        to the value for `cpeLocalIdentifierType`.

        If you don't provide a value when creating the IPSec connection, the `ipAddress` attribute
        for the :class:`Cpe` object specified by `cpeId` is used as the `cpeLocalIdentifier`.

        For information about why you'd provide this value, see
        `If Your CPE Is Behind a NAT Device`__.

        Example IP address: `10.0.3.3`

        Example hostname: `cpe.example.com`

        __ https://docs.cloud.oracle.com/Content/Network/Tasks/overviewIPsec.htm#nat


        :param cpe_local_identifier: The cpe_local_identifier of this IPSecConnection.
        :type: str
        """
        self._cpe_local_identifier = cpe_local_identifier

    @property
    def cpe_local_identifier_type(self):
        """
        Gets the cpe_local_identifier_type of this IPSecConnection.
        The type of identifier for your CPE device. The value here must correspond to the value
        for `cpeLocalIdentifier`.

        Allowed values for this property are: "IP_ADDRESS", "HOSTNAME", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The cpe_local_identifier_type of this IPSecConnection.
        :rtype: str
        """
        return self._cpe_local_identifier_type

    @cpe_local_identifier_type.setter
    def cpe_local_identifier_type(self, cpe_local_identifier_type):
        """
        Sets the cpe_local_identifier_type of this IPSecConnection.
        The type of identifier for your CPE device. The value here must correspond to the value
        for `cpeLocalIdentifier`.


        :param cpe_local_identifier_type: The cpe_local_identifier_type of this IPSecConnection.
        :type: str
        """
        allowed_values = ["IP_ADDRESS", "HOSTNAME"]
        if not value_allowed_none_or_none_sentinel(cpe_local_identifier_type, allowed_values):
            cpe_local_identifier_type = 'UNKNOWN_ENUM_VALUE'
        self._cpe_local_identifier_type = cpe_local_identifier_type

    @property
    def static_routes(self):
        """
        **[Required]** Gets the static_routes of this IPSecConnection.
        Static routes to the CPE. The CIDR must not be a
        multicast address or class E address.

        Used for routing a given IPSec tunnel's traffic only if the tunnel
        is using static routing. If you configure at least one tunnel to use static routing, then
        you must provide at least one valid static route. If you configure both
        tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.


        Example: `10.0.1.0/24`


        :return: The static_routes of this IPSecConnection.
        :rtype: list[str]
        """
        return self._static_routes

    @static_routes.setter
    def static_routes(self, static_routes):
        """
        Sets the static_routes of this IPSecConnection.
        Static routes to the CPE. The CIDR must not be a
        multicast address or class E address.

        Used for routing a given IPSec tunnel's traffic only if the tunnel
        is using static routing. If you configure at least one tunnel to use static routing, then
        you must provide at least one valid static route. If you configure both
        tunnels to use BGP dynamic routing, you can provide an empty list for the static routes.


        Example: `10.0.1.0/24`


        :param static_routes: The static_routes of this IPSecConnection.
        :type: list[str]
        """
        self._static_routes = static_routes

    @property
    def time_created(self):
        """
        Gets the time_created of this IPSecConnection.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this IPSecConnection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IPSecConnection.
        The date and time the IPSec connection was created, in the format defined by RFC3339.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this IPSecConnection.
        :type: datetime
        """
        self._time_created = time_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other