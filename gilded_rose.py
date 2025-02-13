# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class ItemBehavior:
    def improve_quality(self, item, amount):
        item.quality = min(50, item.quality + amount)

    def degrade_quality(self, item, amount):
        item.quality = max(0, item.quality - amount)

    def decrease_sell_in(self, item):
        item.sell_in -= 1


class NormalItemBehavior(ItemBehavior):
    def update(self, item):
        self.decrease_sell_in(item)
        self.degrade_quality(item, 2 if item.sell_in < 0 else 1)

class AgedBrieBehavior(ItemBehavior):
    def update(self, item):
        self.decrease_sell_in(item)
        increment = 2 if item.sell_in < 0 else 1  # Ensure it increments by 2 post sell-by date
        self.improve_quality(item, increment)

class BackstageBehavior(ItemBehavior):
    def update(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            self.improve_quality(item, 3)
        elif item.sell_in < 10:
            self.improve_quality(item, 2)
        else:
            self.improve_quality(item, 1)


class ConjuredBehavior(ItemBehavior):
    def update(self, item):
        self.decrease_sell_in(item)
        decrement = 4 if item.sell_in < 0 else 2  # Ensure it degrades by 2 before sell-by
        self.degrade_quality(item, decrement)


class SulfurasBehavior(ItemBehavior):
    def update(self, item):
        pass  # No changes for Sulfuras




class GildedRose:
    def __init__(self, items):
        self.items = items
        self.behaviors = {
            "Aged Brie": AgedBrieBehavior(),
            "Backstage passes to a TAFKAL80ETC concert": BackstageBehavior(),
            "Sulfuras, Hand of Ragnaros": SulfurasBehavior(),
            "Conjured Mana Cake": ConjuredBehavior(),  
            # Default behavior for normal items
            "default": NormalItemBehavior()
        }

    def update_quality(self):
        for item in self.items:
            behavior = self.behaviors.get(item.name, self.behaviors["default"])
            behavior.update(item)
    def get_items(self):
        return [item.name for item in self.items]
    def get_items_by_quality_threshold(self, threshold):
        return [item for item in self.items if item.quality > threshold]