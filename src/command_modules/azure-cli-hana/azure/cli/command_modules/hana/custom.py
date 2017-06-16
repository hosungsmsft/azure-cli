# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import azure.cli.core.azlogging as azlogging


logger = azlogging.get_az_logger(__name__)


def hana_list(resource_group=None):
    result = {'resource_group': resource_group}
    return result


def hana_show(resource_group, instance_name):
    return {'resource_group': resource_group, 'hana_instance_name': instance_name}
