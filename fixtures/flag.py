#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Include this to load these fixtures. """

def import_fixtures(self):
    """ Create simple fixture entries..."""
    self.redis.zadd('flag_border', {'{ "name":"solid", "score":100  }': 100})
    self.redis.zadd('flag_division', {'{ "name":"stripes", "score":100  }': 100})
    self.redis.zadd('flag_overlay', {'{ "name":"rays", "score":100  }': 100})
    self.redis.zadd('flag_ratio', {'{ "name":"2.55", "score":100  }': 100})
    self.redis.zadd('flag_shape', {'{"name":"tongued",     "score":100   }': 100})
    self.redis.zadd('flag_symbol', {'{ "name":"letter", "score":100  }': 100})

    self.redis.lpush('flag_border_solid_size', '.01')
    self.redis.lpush('flagcolor', 'black')
    self.redis.lpush('flagcolor', 'brown')
    self.redis.lpush('flagcolor', 'darkbrown')
    self.redis.lpush('flagcolor', 'lightred')

    self.redis.lpush('flagcolor', 'purple')
    self.redis.lpush('flagcolor', 'red')
    self.redis.lpush('flagcolor', 'verylightred')
    self.redis.lpush('flagcolor', 'white')
    self.redis.lpush('flag_division_diagonal_direction', 'left-to-right')
    self.redis.lpush('flag_division_stripes_colorcount', '2')
    self.redis.lpush('flag_division_stripes_count', '3')
    self.redis.lpush('flag_division_stripes_side', 'horizontal')
    import_color_fixtures(self)
    import_overlay_fixtures(self)
    import_shape_fixtures(self)
    import_symbol_fixtures(self)

def import_color_fixtures(self):
    """ Create flag color fixture entries..."""
    self.redis.hset('flagcolor_description', 'black',
                    '{"name":"black",             "hex":"#000000",  "verb":"destroy",    "adverb":"purposefully"     }')
    self.redis.hset('flagcolor_description', 'brown',
                    '{"name":"brown",             "hex":"#663300",  "verb":"withstand",  "adverb":"solidly"          }')
    self.redis.hset('flagcolor_description', 'darkbrown',
                    '{"name":"dark brown",        "hex":"#330000",  "verb":"balance",    "adverb":"naturally"        }')
    self.redis.hset('flagcolor_description', 'lightred',
                    '{"name":"light red",         "hex":"#ff3333",  "verb":"cherish",    "adverb":"peacefully"       }')
    self.redis.hset('flagcolor_description', 'purple',
                    '{"name":"purple",            "hex":"#660099",  "verb":"rule",       "adverb":"majestically"     }')
    self.redis.hset('flagcolor_description', 'red',
                    '{"name":"red",               "hex":"#ff0000",  "verb":"expand",     "adverb":"gracefully"       }')
    self.redis.hset('flagcolor_description', 'verylightred',
                    '{"name":"very light red",    "hex":"#ff6666",  "verb":"love",       "adverb":"lovingly"         }')
    self.redis.hset('flagcolor_description', 'white',
                    '{"name":"white",             "hex":"#ffffff",  "verb":"perfect",    "adverb":"peacefully"       }')

def import_overlay_fixtures(self):
    """ Create flag overlay fixture entries..."""
    self.redis.lpush('flag_overlay_circle_outline', 'false')
    self.redis.lpush('flag_overlay_circle_outlinewidth', '5')
    self.redis.lpush('flag_overlay_circle_radius', '.333')
    self.redis.lpush('flag_overlay_circle_radiusdirection', 'vertical')
    self.redis.lpush('flag_overlay_circle_x', '-1')
    self.redis.lpush('flag_overlay_circle_y', '.75')
    self.redis.lpush('flag_overlay_cross_horlength', '0.5')
    self.redis.lpush('flag_overlay_cross_horpos', '0.33')
    self.redis.lpush('flag_overlay_cross_horwidth', '0.2')
    self.redis.lpush('flag_overlay_cross_vertwidth', '0.05')
    self.redis.lpush('flag_overlay_diamond_outline', 'true')
    self.redis.lpush('flag_overlay_quaddiag_side', 'south')
    self.redis.lpush('flag_overlay_rays_count', '5')
    self.redis.lpush('flag_overlay_rays_offset', '.05')
    self.redis.lpush('flag_overlay_rays_x', '.25')
    self.redis.lpush('flag_overlay_rays_y', '.25')
    self.redis.lpush('flag_overlay_slash_direction', 'left-to-right')
    self.redis.lpush('flag_overlay_slash_width', '0.15')
    self.redis.lpush('flag_overlay_stripe_count', '2')
    self.redis.lpush('flag_overlay_stripe_side', 'horizontal')
    self.redis.lpush('flag_overlay_x_outline', 'false')
    self.redis.lpush('flag_overlay_x_width', '0.15')

def import_shape_fixtures(self):
    """ Create flag shape fixture entries..."""
    self.redis.lpush('flag_shape_swallow_depth', '30')
    self.redis.lpush('flag_shape_tongued_count', '11')
    self.redis.lpush('flag_shape_tongued_depth', '0.2')
    self.redis.lpush('flag_shape_tongued_shape', 'scallop')

def import_symbol_fixtures(self):
    """ Create flag symbol fixture entries..."""
    self.redis.lpush('flag_symbol_circle_outline', 'true')
    self.redis.lpush('flag_symbol_circle_radius', '.25')
    self.redis.lpush('flag_symbol_circle_radiusdirection', 'vertical')
    self.redis.lpush('flag_symbol_circle_x', '.25')
    self.redis.lpush('flag_symbol_circle_y', '.5')
    self.redis.lpush('flag_symbol_letter_fontfamily', 'Verdana Bold Italic')
    self.redis.lpush('flag_symbol_letter_size', '.25')
    self.redis.lpush('flag_symbol_letter_x', '.5')
    self.redis.lpush('flag_symbol_letter_y', '.5')
    self.redis.lpush('flag_symbol_star_inset', '.25')
    self.redis.lpush('flag_symbol_star_points', '4')
    self.redis.lpush('flag_symbol_star_x', '.5')
    self.redis.lpush('flag_symbol_star_y', '.5')
