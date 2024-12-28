from aws_cdk import (
    # Duration,
    Stack,
    aws_iot as iot,Tags,
)
from constructs import Construct

class IotBillingGroupStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an IoT billing group
        billing_group = iot.CfnBillingGroup(self, "RSTBillingGroup",
            billing_group_name="RST-billing-group",
            billing_group_properties=iot.CfnBillingGroup.BillingGroupPropertiesProperty(
                billing_group_description="RST billing group for IoT"
            )
        )
        # Add tags to the billing group
        Tags.of(billing_group).add("Appname", "RST")
        Tags.of(billing_group).add("AppId", "38080")
        Tags.of(billing_group).add("Env", "Dev")
