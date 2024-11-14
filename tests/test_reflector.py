import pytest
import os
import platform

from utils import (
    microk8s_disable,
    microk8s_enable,
    wait_for_pod_state,
)


class TestReflector(object):
    @pytest.mark.skipif(platform.machine() == "s390x", reason="Not available on s390x")
    @pytest.mark.skipif(
        os.environ.get("UNDER_TIME_PRESSURE") == None,
        reason="Skipping test, expected to be tested when under time pressure",
    )
    def test_reflector(self):
        """
        Sets up and validates reflector.
        """
        print("Enabling reflector")
        microk8s_enable("reflector")
        print("Validating reflector")
        self.validate_reflector()
        print("Disabling reflector")
        microk8s_disable("reflector")

    def validate_reflector(self):
        """
        Validate reflector
        """
        wait_for_pod_state(
            "", "reflector", "running", label="app.kubernetes.io/name=reflector"
        )
        print("reflector is up and running")

