#!/usr/bin/env python
# encoding: utf-8

from __future__ import absolute_import, division
from imp import load_source
from unittest import TestCase, main

menu = load_source('menu', 'menu')


class EndUserTests(TestCase):

    def test_simple_clicks_work(self):
        result = menu.argv_to_applescript(['menu.py', 'app', 'menu', 'item'])
        self.assertEqual(result, """
tell application "System Events"
    tell application "app"
        tell menu bar 1
            tell menu bar item "menu"
                tell menu "menu"
                    click menu item "item"
                end tell
            end tell
        end tell
    end tell
end tell
"""[1:-1])

    def test_nested_clicks_work(self):
        result = menu.argv_to_applescript(['menu.py', 'app', 'menu',
                                           'submenu', 'item'])
        self.assertEqual(result, """
tell application "System Events"
    tell application "app"
        tell menu bar 1
            tell menu bar item "menu"
                tell menu "menu"
                    tell menu bar item "submenu"
                        tell menu "submenu"
                            click menu item "item"
                        end tell
                    end tell
                end tell
            end tell
        end tell
    end tell
end tell
"""[1:-1])


if __name__ == '__main__':
    main()
