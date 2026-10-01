"""个性动作 - 带7个bug"""
from dataclasses import dataclass, field
import time

@dataclass
class Emote:
    eid: str
    name: str
    duration: float
    unlock_level: int
    is_interactive: bool

class EmoteSystem:
    def __init__(self):
        self.emotes: dict[str, Emote] = {}
        self.last_use = {}
        self.favorites = {}

    def use(self, player_id, emote_id):
        # bug1: 无冷却
        self.last_use[player_id] = time.time()
        return True

    def can_unlock(self, player_id, level, achievements):
        # bug2: 只看等级
        return level >= self.emotes[emote_id].unlock_level

    def interactive(self, from_id, to_id, emote_id):
        # bug3: 不检查对方状态
        return True

    def get_duration(self, emote_id):
        # bug4: 固定
        return 5

    def cancel(self, player_id, emote_id):
        # bug5: 不能取消
        return False

    def use_text_only(self, player_id, emote_id):
        # bug6: 表情文字绑定
        emote = self.emotes[emote_id]
        return {"emote": emote.name, "text": emote.name}

    def add_favorite(self, player_id, emote_id):
        # bug7: 无上限
        if player_id not in self.favorites:
            self.favorites[player_id] = []
        self.favorites[player_id].append(emote_id)
