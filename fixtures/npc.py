
def import_fixtures(self):
    self.redis.zadd( 'npc_sex', '{"name":"female",     "pronoun":"she", "possessive":"her", "third-person":"her", "spouse":"husband", "score":51   }', 100);
    self.redis.zadd('npc_piety','{"name":"overzealous",   "score":100   }',100)
    self.redis.zadd('npc_age','{"name":"ancient",        "score":100 }',100)
    self.redis.zadd('npc_honor','{"name":"honorable",     "score":100 }',100)
    self.redis.zadd('npc_bravery','{"name":"heroic",   "score":100  }',100)
    self.redis.zadd('npc_skill','{"name":"legendarily skilled",   "score":100  }',100)
    self.redis.zadd('npc_experience','{"name":"grizzled",   "score":100  }',100)
    self.redis.zadd('npc_strength','{"name":"herculean",   "score":100  }',100)
    self.redis.zadd('npc_endurance','{"name":"unflagging",   "score":100  }',100)
    self.redis.zadd('npc_satisfaction','{"name":"satisfied",   "score":100  }',100)
    self.redis.zadd('npc_agility','{"name":"agile",   "score":100  }',100)
    self.redis.zadd('npc_wisdom','{"name":"wise",   "score":100  }',100)
    self.redis.zadd('npc_charisma','{"name":"inspiring",   "score":100  }',100)
    self.redis.zadd('npc_intelligence','{"name":"brilliant",   "score":100  }',100)
    self.redis.zadd('npc_attractiveness','{"name":"stunning",     "score":100 }',100)
    self.redis.zadd('npc_money','{"name":"rich",             "score":100 }',100)
    self.redis.zadd('npc_generous','{"name":"generous",     "score":100 }',100)
    self.redis.zadd('npc_luck','{"name":"lucky",          "score":100 }',100)
    self.redis.zadd('npc_confident','{"name":"incredibly",     "score":100 }',100)
    self.redis.zadd('npc_kill','{"name":"killed without issue",             "score":100  }',100)
    self.redis.lpush('npc_medical_condition', 'deafness in one ear')

    self.redis.lpush('npc_posessiondetail','was lost during the war')
    self.redis.lpush('npc_posession','jackknife')
    self.redis.lpush('npc_attitude','cautious')
    self.redis.lpush('npc_regret','scared a child')
    self.redis.lpush('npc_height','short')
    self.redis.lpush('npc_build','thin')
    self.redis.lpush('npc_mark','mole')
    self.redis.lpush('npc_mark_location','face')
    self.redis.lpush('npc_complexion','dull')
    self.redis.lpush('npc_eye','beady')
    self.redis.lpush('npc_profession','actor')
    self.redis.lpush('npc_emotion','angry')
    self.redis.lpush('npc_marriagestatus','divorced')
    self.redis.lpush('npc_modeical_condition','gout')
    self.redis.lpush('fur_covertemplate','fur cover template')
    self.redis.lpush('fur_furcolor','blue')
    self.redis.lpush('fur_furkind','soft')
    self.redis.lpush('skin_covertemplate','skin cover template')
    self.redis.lpush('skin_skincolor','red')
    self.redis.lpush('skin_skinkind','scabby')
    self.redis.lpush('scale_covertemplate','scale cover template')
    self.redis.lpush('scale_scalecolor','silver')
    self.redis.lpush('scale_scalekind','flaky')
    self.redis.lpush('feather_covertemplate','feather cover template')
    self.redis.lpush('feather_feathercolor','white')
    self.redis.lpush('feather_featherkind','thin')

    #Details for Kobolds
    self.redis.set( 'kobold_details', '{"name": "Kobold",     "size": "small",   "description": "their small stature and cowardice"}')
    self.redis.lpush('kobold_covering','skin')
    self.redis.lpush('koboldname_fullname_template', '{{params.title}} {{params.first_root}}{{params.first_post}} {{params.trailer}}')
    self.redis.lpush('koboldname_shortname_template', '{{params.first_root}}')
    self.redis.lpush('koboldname_formalname_template', '{{params.title}} {{params.first_root}}')

    self.redis.set('kobold_subrace_chance',100)
    self.redis.lpush('kobold_subrace', 'aquatic')
    self.redis.hset('kobold_subrace_description', 'aquatic', '{"subrace": "Aquatic Kobold",   "description": "" }')

    self.redis.lpush('koboldname_first_root', 'Kole')

    #Details for Humans
    self.redis.set('human_details', '{"name": "Human",  "size": "medium",  "description": "quick growth and adaptability"}')
    #details for Humans
    self.redis.lpush('human_covering','skin')

    self.redis.lpush('humanname_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}}{{params.first_post}} {{params.last_pre}}{{params.last_root}}{{params.last_post}} {{params.trailer}}')
    self.redis.lpush('humanname_shortname_template', '{{params.first_pre}}{{params.first_root}}{{params.first_post}}')
    self.redis.lpush('humanname_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}{{params.last_post}}')

    self.redis.lpush('humanname_first_pre', 'Dru')
    self.redis.lpush('humanname_first_root', 'cil')
    self.redis.lpush('humanname_first_post', 'la')
    self.redis.lpush('humanname_last_pre', 'La')
    self.redis.lpush('humanname_last_root', 'Sal')
    self.redis.lpush('humanname_last_post', 'vae')






    #Details for Kobolds
    self.redis.set('gnome_details',  '{"name": "Gnome",      "size": "small",   "description": "having engineering and intellectual expertise" }')
    self.redis.lpush('gnome_covering','skin')
    self.redis.lpush('gnomename_fullname_template', '{{params.title}} {{params.first_pre}}{{params.first_root}} {{params.last_pre}}{{params.last_root}} {{params.trailer}}')
    self.redis.lpush('gnomename_shortname_template', '{{params.first_pre}}{{params.first_root}}')
    self.redis.lpush('gnomename_formalname_template', '{{params.title}} {{params.last_pre}}{{params.last_root}}')
    self.redis.lpush('gnomename_first_root', 'Tom')
    self.redis.lpush('gnomename_last_pre', 'Gyro')

