# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08my.proto\x12 bilibili.community.service.dm.v1\"X\n\x0e\x42uzzwordConfig\x12\x46\n\x08keywords\x18\x01 \x03(\x0b\x32\x34.bilibili.community.service.dm.v1.BuzzwordShowConfig\"x\n\x12\x42uzzwordShowConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\x05\x12\n\n\x02id\x18\x04 \x01(\x03\x12\x13\n\x0b\x62uzzword_id\x18\x05 \x01(\x03\x12\x13\n\x0bschema_type\x18\x06 \x01(\x05\"\xa1\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\t\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\r\n\x05idStr\x18\n \x01(\t\"P\n\rDanmakuAIFlag\x12?\n\x08\x64m_flags\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuFlag\"\xd6\x01\n\x0b\x44\x61nmakuElem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x10\n\x08progress\x18\x02 \x01(\x05\x12\x0c\n\x04mode\x18\x03 \x01(\x05\x12\x10\n\x08\x66ontsize\x18\x04 \x01(\x05\x12\r\n\x05\x63olor\x18\x05 \x01(\r\x12\x0f\n\x07midHash\x18\x06 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x07 \x01(\t\x12\r\n\x05\x63time\x18\x08 \x01(\x03\x12\x0e\n\x06weight\x18\t \x01(\x05\x12\x0e\n\x06\x61\x63tion\x18\n \x01(\t\x12\x0c\n\x04pool\x18\x0b \x01(\x05\x12\r\n\x05idStr\x18\x0c \x01(\t\x12\x0c\n\x04\x61ttr\x18\r \x01(\x05\")\n\x0b\x44\x61nmakuFlag\x12\x0c\n\x04\x64mid\x18\x01 \x01(\x03\x12\x0c\n\x04\x66lag\x18\x02 \x01(\r\"K\n\x11\x44\x61nmakuFlagConfig\x12\x10\n\x08rec_flag\x18\x01 \x01(\x05\x12\x10\n\x08rec_text\x18\x02 \x01(\t\x12\x12\n\nrec_switch\x18\x03 \x01(\x05\"\xcc\x04\n\x18\x44\x61nmuDefaultPlayerConfig\x12)\n!player_danmaku_use_default_config\x18\x01 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12$\n\x1cinline_player_danmaku_switch\x18\x10 \x01(\x08\x12)\n!player_danmaku_senior_mode_switch\x18\x11 \x01(\x05\"\xfe\x05\n\x11\x44\x61nmuPlayerConfig\x12\x1d\n\x15player_danmaku_switch\x18\x01 \x01(\x08\x12\"\n\x1aplayer_danmaku_switch_save\x18\x02 \x01(\x08\x12)\n!player_danmaku_use_default_config\x18\x03 \x01(\x08\x12,\n$player_danmaku_ai_recommended_switch\x18\x04 \x01(\x08\x12+\n#player_danmaku_ai_recommended_level\x18\x05 \x01(\x05\x12\x1f\n\x17player_danmaku_blocktop\x18\x06 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockscroll\x18\x07 \x01(\x08\x12\"\n\x1aplayer_danmaku_blockbottom\x18\x08 \x01(\x08\x12$\n\x1cplayer_danmaku_blockcolorful\x18\t \x01(\x08\x12\"\n\x1aplayer_danmaku_blockrepeat\x18\n \x01(\x08\x12#\n\x1bplayer_danmaku_blockspecial\x18\x0b \x01(\x08\x12\x1e\n\x16player_danmaku_opacity\x18\x0c \x01(\x02\x12$\n\x1cplayer_danmaku_scalingfactor\x18\r \x01(\x02\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\x12\x1c\n\x14player_danmaku_speed\x18\x0f \x01(\x05\x12&\n\x1eplayer_danmaku_enableblocklist\x18\x10 \x01(\x08\x12$\n\x1cinline_player_danmaku_switch\x18\x11 \x01(\x08\x12$\n\x1cinline_player_danmaku_config\x18\x12 \x01(\x05\x12&\n\x1eplayer_danmaku_ios_switch_save\x18\x13 \x01(\x05\x12)\n!player_danmaku_senior_mode_switch\x18\x14 \x01(\x05\"K\n\x18\x44\x61nmuPlayerDynamicConfig\x12\x10\n\x08progress\x18\x01 \x01(\x05\x12\x1d\n\x15player_danmaku_domain\x18\x0e \x01(\x02\"\xb1\x02\n\x15\x44\x61nmuPlayerViewConfig\x12\x61\n\x1d\x64\x61nmuku_default_player_config\x18\x01 \x01(\x0b\x32:.bilibili.community.service.dm.v1.DanmuDefaultPlayerConfig\x12R\n\x15\x64\x61nmuku_player_config\x18\x02 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmuPlayerConfig\x12\x61\n\x1d\x64\x61nmuku_player_dynamic_config\x18\x03 \x03(\x0b\x32:.bilibili.community.service.dm.v1.DanmuPlayerDynamicConfig\"\xab\x03\n\x14\x44\x61nmuWebPlayerConfig\x12\x11\n\tdm_switch\x18\x01 \x01(\x08\x12\x11\n\tai_switch\x18\x02 \x01(\x08\x12\x10\n\x08\x61i_level\x18\x03 \x01(\x05\x12\x10\n\x08\x62locktop\x18\x04 \x01(\x08\x12\x13\n\x0b\x62lockscroll\x18\x05 \x01(\x08\x12\x13\n\x0b\x62lockbottom\x18\x06 \x01(\x08\x12\x12\n\nblockcolor\x18\x07 \x01(\x08\x12\x14\n\x0c\x62lockspecial\x18\x08 \x01(\x08\x12\x14\n\x0cpreventshade\x18\t \x01(\x08\x12\r\n\x05\x64mask\x18\n \x01(\x08\x12\x0f\n\x07opacity\x18\x0b \x01(\x02\x12\x0e\n\x06\x64marea\x18\x0c \x01(\x05\x12\x11\n\tspeedplus\x18\r \x01(\x02\x12\x10\n\x08\x66ontsize\x18\x0e \x01(\x02\x12\x12\n\nscreensync\x18\x0f \x01(\x08\x12\x11\n\tspeedsync\x18\x10 \x01(\x08\x12\x12\n\nfontfamily\x18\x11 \x01(\t\x12\x0c\n\x04\x62old\x18\x12 \x01(\x08\x12\x12\n\nfontborder\x18\x13 \x01(\x05\x12\x11\n\tdraw_type\x18\x14 \x01(\t\x12\x1a\n\x12senior_mode_switch\x18\x15 \x01(\x05\"A\n\x0f\x44mExpoReportReq\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\r\n\x05spmid\x18\x04 \x01(\t\"\x11\n\x0f\x44mExpoReportRes\"\xfd\x0b\n\x11\x44mPlayerConfigReq\x12\n\n\x02ts\x18\x01 \x01(\x03\x12\x45\n\x06switch\x18\x02 \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuSwitch\x12N\n\x0bswitch_save\x18\x03 \x01(\x0b\x32\x39.bilibili.community.service.dm.v1.PlayerDanmakuSwitchSave\x12[\n\x12use_default_config\x18\x04 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuUseDefaultConfig\x12\x61\n\x15\x61i_recommended_switch\x18\x05 \x01(\x0b\x32\x42.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedSwitch\x12_\n\x14\x61i_recommended_level\x18\x06 \x01(\x0b\x32\x41.bilibili.community.service.dm.v1.PlayerDanmakuAiRecommendedLevel\x12I\n\x08\x62locktop\x18\x07 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.PlayerDanmakuBlocktop\x12O\n\x0b\x62lockscroll\x18\x08 \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockscroll\x12O\n\x0b\x62lockbottom\x18\t \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockbottom\x12S\n\rblockcolorful\x18\n \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuBlockcolorful\x12O\n\x0b\x62lockrepeat\x18\x0b \x01(\x0b\x32:.bilibili.community.service.dm.v1.PlayerDanmakuBlockrepeat\x12Q\n\x0c\x62lockspecial\x18\x0c \x01(\x0b\x32;.bilibili.community.service.dm.v1.PlayerDanmakuBlockspecial\x12G\n\x07opacity\x18\r \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.PlayerDanmakuOpacity\x12S\n\rscalingfactor\x18\x0e \x01(\x0b\x32<.bilibili.community.service.dm.v1.PlayerDanmakuScalingfactor\x12\x45\n\x06\x64omain\x18\x0f \x01(\x0b\x32\x35.bilibili.community.service.dm.v1.PlayerDanmakuDomain\x12\x43\n\x05speed\x18\x10 \x01(\x0b\x32\x34.bilibili.community.service.dm.v1.PlayerDanmakuSpeed\x12W\n\x0f\x65nableblocklist\x18\x11 \x01(\x0b\x32>.bilibili.community.service.dm.v1.PlayerDanmakuEnableblocklist\x12^\n\x19inlinePlayerDanmakuSwitch\x18\x12 \x01(\x0b\x32;.bilibili.community.service.dm.v1.InlinePlayerDanmakuSwitch\x12[\n\x12senior_mode_switch\x18\x13 \x01(\x0b\x32?.bilibili.community.service.dm.v1.PlayerDanmakuSeniorModeSwitch\"/\n\x0b\x44mSegConfig\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\r\n\x05total\x18\x02 \x01(\x03\"\xa1\x01\n\x10\x44mSegMobileReply\x12<\n\x05\x65lems\x18\x01 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\x12\r\n\x05state\x18\x02 \x01(\x05\x12@\n\x07\x61i_flag\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.DanmakuAIFlag\"g\n\x0e\x44mSegMobileReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\x12\x16\n\x0eteenagers_mode\x18\x05 \x01(\x05\"]\n\rDmSegOttReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegOttReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"]\n\rDmSegSDKReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12<\n\x05\x65lems\x18\x02 \x03(\x0b\x32-.bilibili.community.service.dm.v1.DanmakuElem\"L\n\x0b\x44mSegSDKReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x15\n\rsegment_index\x18\x04 \x01(\x03\"\xc2\x05\n\x0b\x44mViewReply\x12\x0e\n\x06\x63losed\x18\x01 \x01(\x08\x12\x39\n\x04mask\x18\x02 \x01(\x0b\x32+.bilibili.community.service.dm.v1.VideoMask\x12\x41\n\x08subtitle\x18\x03 \x01(\x0b\x32/.bilibili.community.service.dm.v1.VideoSubtitle\x12\x13\n\x0bspecial_dms\x18\x04 \x03(\t\x12\x44\n\x07\x61i_flag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12N\n\rplayer_config\x18\x06 \x01(\x0b\x32\x37.bilibili.community.service.dm.v1.DanmuPlayerViewConfig\x12\x16\n\x0esend_box_style\x18\x07 \x01(\x05\x12\r\n\x05\x61llow\x18\x08 \x01(\x08\x12\x11\n\tcheck_box\x18\t \x01(\t\x12\x1a\n\x12\x63heck_box_show_msg\x18\n \x01(\t\x12\x18\n\x10text_placeholder\x18\x0b \x01(\t\x12\x19\n\x11input_placeholder\x18\x0c \x01(\t\x12\x1d\n\x15report_filter_content\x18\r \x03(\t\x12\x41\n\x0b\x65xpo_report\x18\x0e \x01(\x0b\x32,.bilibili.community.service.dm.v1.ExpoReport\x12I\n\x0f\x62uzzword_config\x18\x0f \x01(\x0b\x32\x30.bilibili.community.service.dm.v1.BuzzwordConfig\x12\x42\n\x0b\x65xpressions\x18\x10 \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\"X\n\tDmViewReq\x12\x0b\n\x03pid\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x14\n\x0cis_hard_boot\x18\x05 \x01(\x05\"\xec\x03\n\x0e\x44mWebViewReply\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\ttext_side\x18\x03 \x01(\t\x12=\n\x06\x64m_sge\x18\x04 \x01(\x0b\x32-.bilibili.community.service.dm.v1.DmSegConfig\x12\x41\n\x04\x66lag\x18\x05 \x01(\x0b\x32\x33.bilibili.community.service.dm.v1.DanmakuFlagConfig\x12\x13\n\x0bspecial_dms\x18\x06 \x03(\t\x12\x11\n\tcheck_box\x18\x07 \x01(\x08\x12\r\n\x05\x63ount\x18\x08 \x01(\x03\x12?\n\ncommandDms\x18\t \x03(\x0b\x32+.bilibili.community.service.dm.v1.CommandDm\x12M\n\rplayer_config\x18\n \x01(\x0b\x32\x36.bilibili.community.service.dm.v1.DanmuWebPlayerConfig\x12\x1d\n\x15report_filter_content\x18\x0b \x03(\t\x12\x42\n\x0b\x65xpressions\x18\x0c \x03(\x0b\x32-.bilibili.community.service.dm.v1.Expressions\"*\n\nExpoReport\x12\x1c\n\x14should_report_at_end\x18\x01 \x01(\x08\"d\n\nExpression\x12\x0f\n\x07keyword\x18\x01 \x03(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x38\n\x06period\x18\x03 \x03(\x0b\x32(.bilibili.community.service.dm.v1.Period\"I\n\x0b\x45xpressions\x12:\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32,.bilibili.community.service.dm.v1.Expression\"$\n\x06Period\x12\r\n\x05start\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\"*\n\x19InlinePlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\"0\n\x1fPlayerDanmakuAiRecommendedLevel\x12\r\n\x05value\x18\x01 \x01(\x08\"1\n PlayerDanmakuAiRecommendedSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockbottom\x12\r\n\x05value\x18\x01 \x01(\x08\"+\n\x1aPlayerDanmakuBlockcolorful\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockrepeat\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x18PlayerDanmakuBlockscroll\x12\r\n\x05value\x18\x01 \x01(\x08\"*\n\x19PlayerDanmakuBlockspecial\x12\r\n\x05value\x18\x01 \x01(\x08\"&\n\x15PlayerDanmakuBlocktop\x12\r\n\x05value\x18\x01 \x01(\x08\"$\n\x13PlayerDanmakuDomain\x12\r\n\x05value\x18\x01 \x01(\x02\"-\n\x1cPlayerDanmakuEnableblocklist\x12\r\n\x05value\x18\x01 \x01(\x08\"%\n\x14PlayerDanmakuOpacity\x12\r\n\x05value\x18\x01 \x01(\x02\"+\n\x1aPlayerDanmakuScalingfactor\x12\r\n\x05value\x18\x01 \x01(\x02\".\n\x1dPlayerDanmakuSeniorModeSwitch\x12\r\n\x05value\x18\x01 \x01(\x05\"#\n\x12PlayerDanmakuSpeed\x12\r\n\x05value\x18\x01 \x01(\x05\"7\n\x13PlayerDanmakuSwitch\x12\r\n\x05value\x18\x01 \x01(\x08\x12\x11\n\tcanIgnore\x18\x02 \x01(\x08\"(\n\x17PlayerDanmakuSwitchSave\x12\r\n\x05value\x18\x01 \x01(\x08\".\n\x1dPlayerDanmakuUseDefaultConfig\x12\r\n\x05value\x18\x01 \x01(\x08\")\n\x08Response\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"\xd8\x01\n\x0cSubtitleItem\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0e\n\x06id_str\x18\x02 \x01(\t\x12\x0b\n\x03lan\x18\x03 \x01(\t\x12\x0f\n\x07lan_doc\x18\x04 \x01(\t\x12\x14\n\x0csubtitle_url\x18\x05 \x01(\t\x12:\n\x06\x61uthor\x18\x06 \x01(\x0b\x32*.bilibili.community.service.dm.v1.UserInfo\x12<\n\x04type\x18\x07 \x01(\x0e\x32..bilibili.community.service.dm.v1.SubtitleType\"\\\n\x08UserInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03sex\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0c\n\x04sign\x18\x05 \x01(\t\x12\x0c\n\x04rank\x18\x06 \x01(\x05\"S\n\tVideoMask\x12\x0b\n\x03\x63id\x18\x01 \x01(\x03\x12\x0c\n\x04plat\x18\x02 \x01(\x05\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x05\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08mask_url\x18\x05 \x01(\t\"o\n\rVideoSubtitle\x12\x0b\n\x03lan\x18\x01 \x01(\t\x12\x0e\n\x06lanDoc\x18\x02 \x01(\t\x12\x41\n\tsubtitles\x18\x03 \x03(\x0b\x32..bilibili.community.service.dm.v1.SubtitleItem*L\n\tDMAttrBit\x12\x14\n\x10\x44MAttrBitProtect\x10\x00\x12\x15\n\x11\x44MAttrBitFromLive\x10\x01\x12\x12\n\x0e\x44MAttrHighLike\x10\x02*\x1e\n\x0cSubtitleType\x12\x06\n\x02\x43\x43\x10\x00\x12\x06\n\x02\x41I\x10\x01\x32\xa0\x05\n\x02\x44M\x12s\n\x0b\x44mSegMobile\x12\x30.bilibili.community.service.dm.v1.DmSegMobileReq\x1a\x32.bilibili.community.service.dm.v1.DmSegMobileReply\x12\x64\n\x06\x44mView\x12+.bilibili.community.service.dm.v1.DmViewReq\x1a-.bilibili.community.service.dm.v1.DmViewReply\x12q\n\x0e\x44mPlayerConfig\x12\x33.bilibili.community.service.dm.v1.DmPlayerConfigReq\x1a*.bilibili.community.service.dm.v1.Response\x12j\n\x08\x44mSegOtt\x12-.bilibili.community.service.dm.v1.DmSegOttReq\x1a/.bilibili.community.service.dm.v1.DmSegOttReply\x12j\n\x08\x44mSegSDK\x12-.bilibili.community.service.dm.v1.DmSegSDKReq\x1a/.bilibili.community.service.dm.v1.DmSegSDKReply\x12t\n\x0c\x44mExpoReport\x12\x31.bilibili.community.service.dm.v1.DmExpoReportReq\x1a\x31.bilibili.community.service.dm.v1.DmExpoReportResb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DMATTRBIT._serialized_start=8213
  _DMATTRBIT._serialized_end=8289
  _SUBTITLETYPE._serialized_start=8291
  _SUBTITLETYPE._serialized_end=8321
  _BUZZWORDCONFIG._serialized_start=46
  _BUZZWORDCONFIG._serialized_end=134
  _BUZZWORDSHOWCONFIG._serialized_start=136
  _BUZZWORDSHOWCONFIG._serialized_end=256
  _COMMANDDM._serialized_start=259
  _COMMANDDM._serialized_end=420
  _DANMAKUAIFLAG._serialized_start=422
  _DANMAKUAIFLAG._serialized_end=502
  _DANMAKUELEM._serialized_start=505
  _DANMAKUELEM._serialized_end=719
  _DANMAKUFLAG._serialized_start=721
  _DANMAKUFLAG._serialized_end=762
  _DANMAKUFLAGCONFIG._serialized_start=764
  _DANMAKUFLAGCONFIG._serialized_end=839
  _DANMUDEFAULTPLAYERCONFIG._serialized_start=842
  _DANMUDEFAULTPLAYERCONFIG._serialized_end=1430
  _DANMUPLAYERCONFIG._serialized_start=1433
  _DANMUPLAYERCONFIG._serialized_end=2199
  _DANMUPLAYERDYNAMICCONFIG._serialized_start=2201
  _DANMUPLAYERDYNAMICCONFIG._serialized_end=2276
  _DANMUPLAYERVIEWCONFIG._serialized_start=2279
  _DANMUPLAYERVIEWCONFIG._serialized_end=2584
  _DANMUWEBPLAYERCONFIG._serialized_start=2587
  _DANMUWEBPLAYERCONFIG._serialized_end=3014
  _DMEXPOREPORTREQ._serialized_start=3016
  _DMEXPOREPORTREQ._serialized_end=3081
  _DMEXPOREPORTRES._serialized_start=3083
  _DMEXPOREPORTRES._serialized_end=3100
  _DMPLAYERCONFIGREQ._serialized_start=3103
  _DMPLAYERCONFIGREQ._serialized_end=4636
  _DMSEGCONFIG._serialized_start=4638
  _DMSEGCONFIG._serialized_end=4685
  _DMSEGMOBILEREPLY._serialized_start=4688
  _DMSEGMOBILEREPLY._serialized_end=4849
  _DMSEGMOBILEREQ._serialized_start=4851
  _DMSEGMOBILEREQ._serialized_end=4954
  _DMSEGOTTREPLY._serialized_start=4956
  _DMSEGOTTREPLY._serialized_end=5049
  _DMSEGOTTREQ._serialized_start=5051
  _DMSEGOTTREQ._serialized_end=5127
  _DMSEGSDKREPLY._serialized_start=5129
  _DMSEGSDKREPLY._serialized_end=5222
  _DMSEGSDKREQ._serialized_start=5224
  _DMSEGSDKREQ._serialized_end=5300
  _DMVIEWREPLY._serialized_start=5303
  _DMVIEWREPLY._serialized_end=6009
  _DMVIEWREQ._serialized_start=6011
  _DMVIEWREQ._serialized_end=6099
  _DMWEBVIEWREPLY._serialized_start=6102
  _DMWEBVIEWREPLY._serialized_end=6594
  _EXPOREPORT._serialized_start=6596
  _EXPOREPORT._serialized_end=6638
  _EXPRESSION._serialized_start=6640
  _EXPRESSION._serialized_end=6740
  _EXPRESSIONS._serialized_start=6742
  _EXPRESSIONS._serialized_end=6815
  _PERIOD._serialized_start=6817
  _PERIOD._serialized_end=6853
  _INLINEPLAYERDANMAKUSWITCH._serialized_start=6855
  _INLINEPLAYERDANMAKUSWITCH._serialized_end=6897
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_start=6899
  _PLAYERDANMAKUAIRECOMMENDEDLEVEL._serialized_end=6947
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_start=6949
  _PLAYERDANMAKUAIRECOMMENDEDSWITCH._serialized_end=6998
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_start=7000
  _PLAYERDANMAKUBLOCKBOTTOM._serialized_end=7041
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_start=7043
  _PLAYERDANMAKUBLOCKCOLORFUL._serialized_end=7086
  _PLAYERDANMAKUBLOCKREPEAT._serialized_start=7088
  _PLAYERDANMAKUBLOCKREPEAT._serialized_end=7129
  _PLAYERDANMAKUBLOCKSCROLL._serialized_start=7131
  _PLAYERDANMAKUBLOCKSCROLL._serialized_end=7172
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_start=7174
  _PLAYERDANMAKUBLOCKSPECIAL._serialized_end=7216
  _PLAYERDANMAKUBLOCKTOP._serialized_start=7218
  _PLAYERDANMAKUBLOCKTOP._serialized_end=7256
  _PLAYERDANMAKUDOMAIN._serialized_start=7258
  _PLAYERDANMAKUDOMAIN._serialized_end=7294
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_start=7296
  _PLAYERDANMAKUENABLEBLOCKLIST._serialized_end=7341
  _PLAYERDANMAKUOPACITY._serialized_start=7343
  _PLAYERDANMAKUOPACITY._serialized_end=7380
  _PLAYERDANMAKUSCALINGFACTOR._serialized_start=7382
  _PLAYERDANMAKUSCALINGFACTOR._serialized_end=7425
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_start=7427
  _PLAYERDANMAKUSENIORMODESWITCH._serialized_end=7473
  _PLAYERDANMAKUSPEED._serialized_start=7475
  _PLAYERDANMAKUSPEED._serialized_end=7510
  _PLAYERDANMAKUSWITCH._serialized_start=7512
  _PLAYERDANMAKUSWITCH._serialized_end=7567
  _PLAYERDANMAKUSWITCHSAVE._serialized_start=7569
  _PLAYERDANMAKUSWITCHSAVE._serialized_end=7609
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_start=7611
  _PLAYERDANMAKUUSEDEFAULTCONFIG._serialized_end=7657
  _RESPONSE._serialized_start=7659
  _RESPONSE._serialized_end=7700
  _SUBTITLEITEM._serialized_start=7703
  _SUBTITLEITEM._serialized_end=7919
  _USERINFO._serialized_start=7921
  _USERINFO._serialized_end=8013
  _VIDEOMASK._serialized_start=8015
  _VIDEOMASK._serialized_end=8098
  _VIDEOSUBTITLE._serialized_start=8100
  _VIDEOSUBTITLE._serialized_end=8211
  _DM._serialized_start=8324
  _DM._serialized_end=8996
# @@protoc_insertion_point(module_scope)

