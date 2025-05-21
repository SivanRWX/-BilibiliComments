/*
 Navicat Premium Dump SQL

 Source Server         : comments
 Source Server Type    : SQLite
 Source Server Version : 3045000 (3.45.0)
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3045000 (3.45.0)
 File Encoding         : 65001

 Date: 18/05/2025 14:37:59
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for comments
-- ----------------------------
DROP TABLE IF EXISTS "comments";
CREATE TABLE "comments" (
  "username" TEXT NOT NULL,
  "gender" TEXT,
  "post_time" TEXT NOT NULL,
  "content" TEXT,
  "location" TEXT,
  "likes" INTEGER,
  PRIMARY KEY ("username", "post_time")
);

-- ----------------------------
-- Table structure for crawl_status
-- ----------------------------
DROP TABLE IF EXISTS "crawl_status";
CREATE TABLE "crawl_status" (
  "video_oid" TEXT,
  "last_offset" TEXT,
  "last_page" INTEGER,
  "update_time" TIMESTAMP,
  PRIMARY KEY ("video_oid")
);

PRAGMA foreign_keys = true;
