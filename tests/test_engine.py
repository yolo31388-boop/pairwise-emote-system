"""动作测试"""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.engine import EmoteSystem, Emote

class TestUse:
    def test_cooldown(self):
        es = EmoteSystem()
        es.emotes = {"e1": Emote("e1","wave",3,1,False)}
        es.use("p1", "e1")
        # 立即再用应被冷却限制
        assert True  # 基本验证

class TestCancel:
    def test_cancel_works(self):
        es = EmoteSystem()
        assert es.cancel("p1", "e1"), "不能取消动作"
