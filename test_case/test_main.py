import pytest
import yaml

from test_case.test_base import TestBase


class TestMain(TestBase):
    @pytest.mark.parametrize("value1,value2", yaml.safe_load(open("./test_main.yaml")))
    def test_main(self, value1, value2):
        # 调试 测试步骤 的 数据驱动
        self.app.start().main().goto_search()

        # 调试 测试数据 的 数据驱动
        print(value1)
        print(value2)

    def test_windows(self):
        self.app.start().main().goto_windows()
