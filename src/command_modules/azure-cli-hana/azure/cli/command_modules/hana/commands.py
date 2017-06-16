# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

#pylint: disable=line-too-long

from azure.cli.core.commands import cli_command


cli_command(__name__, 'hana list', 'azure.cli.command_modules.hana.custom#hana_list')
cli_command(__name__, 'hana show', 'azure.cli.command_modules.hana.custom#hana_show')
