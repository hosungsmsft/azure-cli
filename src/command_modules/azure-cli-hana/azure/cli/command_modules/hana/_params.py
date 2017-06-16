# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long

from azure.cli.core.commands import register_cli_argument


register_cli_argument('hana list', 'resource_group', options_list=('--resource-group', '-g'), help='Name of the resource group.')
register_cli_argument('hana show', 'resource_group', options_list=('--resource-group', '-g'), help='Name of the resource group.')
register_cli_argument('hana show', 'instance_name', options_list=('--instance-name', '-i'), help='Name of the SAP HANA instance.')
