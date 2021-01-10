#!/usr/bin/env python3
from os.path import basename
import json
import random
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom


def main(argv: list):
    # Parse YouTube Checker json export
    with open(argv[1], "r") as youtube_checker_export:
        youtube_checker = json.load(youtube_checker_export)

    # Create skeleton for Feedbro Subscriptions.opml
    opml = ET.Element("opml", version="1.0")
    head = ET.SubElement(opml, "head")
    ET.SubElement(head, "title").text = "Feed Subscriptions"
    body = ET.SubElement(opml, "body")
    youtube = ET.SubElement(body, "outline", title="YouTube", text="YouTube")

    # Loop through channel ids
    rules = []
    for channel in youtube_checker["channels"]:
        ET.SubElement(
            youtube,
            "outline",
            text=channel["title"],
            title=channel["title"],
            type="rss",
            xmlUrl=f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}",
            htmlUrl=f"https://www.youtube.com/channel/{channel['id']}",
        )

        # Add conditions/filters
        conditions = []
        for filter_ in channel["filters"]:
            conditions.append(
                {
                    "target": "3",
                    "mode": "2",
                    "value": filter_["video_title_pattern"],
                    "casemode": "2",
                }
            )
        if channel["filters"]:
            rules.append(
                {
                    "id": f"{random.randint(1, 9999999999999)}",
                    "schema": 1,
                    "enabled": True,
                    "fallthrough": True,
                    "name": channel["title"],
                    "trigger": "1",
                    "contexttype": "3",
                    "contextvalue": [],
                    "match": "2",
                    "conditions": conditions,
                    "actions": [{"type": "3", "value": ""}],
                    "contextvaluetext": [
                        f"https://www.youtube.com/feeds/videos.xml?channel_id={channel['id']}"
                    ],
                }
            )

    # Write output files
    tree = ET.ElementTree(opml)
    tree.write(
        "Feedbro-YouTube-Checker-Subscriptions.xml",
        encoding="UTF-8",
        xml_declaration=True,
    )
    with open("Feedbro-YouTube-Checker-Subscriptions-Rules.json", "w") as rulesfile:
        json.dump(rules, rulesfile)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {basename(__file__)} YouTube-Checker-Export.json")
        exit(1)
    main(sys.argv)
