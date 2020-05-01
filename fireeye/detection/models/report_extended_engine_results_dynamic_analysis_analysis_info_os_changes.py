# coding: utf-8

"""
    Detection On Demand

    FireEye offers a best-in-class virtual execution engine in many of its core products, including our Network Security, Email Security, and File Analysis solutions. Now our customers can interact with and consume those capabilities directly via a scalable and performant web service. Use the new RESTful API to submit files for malware analysis, search hash values for past analysis results, get full reports for your file submissions, and integrate into your existing toolsets and workflows.  # noqa: E501

    The version of the OpenAPI document: 1.1.1
    Contact: developers@fireeye.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from fireeye.detection.configuration import Configuration


class ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'vm_results': 'list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults]',
        'correlation_results': 'list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults]'
    }

    attribute_map = {
        'vm_results': 'vm_results',
        'correlation_results': 'correlation_results'
    }

    def __init__(self, vm_results=None, correlation_results=None, local_vars_configuration=None):  # noqa: E501
        """ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vm_results = None
        self._correlation_results = None
        self.discriminator = None

        self.vm_results = vm_results
        if correlation_results is not None:
            self.correlation_results = correlation_results

    @property
    def vm_results(self):
        """Gets the vm_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501

        OS Changes split out during DA  # noqa: E501

        :return: The vm_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501
        :rtype: list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults]
        """
        return self._vm_results

    @vm_results.setter
    def vm_results(self, vm_results):
        """Sets the vm_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.

        OS Changes split out during DA  # noqa: E501

        :param vm_results: The vm_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501
        :type: list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesVmResults]
        """
        if self.local_vars_configuration.client_side_validation and vm_results is None:  # noqa: E501
            raise ValueError("Invalid value for `vm_results`, must not be `None`")  # noqa: E501

        self._vm_results = vm_results

    @property
    def correlation_results(self):
        """Gets the correlation_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501

        information related to triggered BALE rules for dynamic analysis work order  # noqa: E501

        :return: The correlation_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501
        :rtype: list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults]
        """
        return self._correlation_results

    @correlation_results.setter
    def correlation_results(self, correlation_results):
        """Sets the correlation_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.

        information related to triggered BALE rules for dynamic analysis work order  # noqa: E501

        :param correlation_results: The correlation_results of this ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges.  # noqa: E501
        :type: list[ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChangesCorrelationResults]
        """

        self._correlation_results = correlation_results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportExtendedEngineResultsDynamicAnalysisAnalysisInfoOsChanges):
            return True

        return self.to_dict() != other.to_dict()
