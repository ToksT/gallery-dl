# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import gelbooru


__tests__ = (
{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=list&tags=bonocho",
    "#category": ("booru", "gelbooru", "tag"),
    "#class"   : gelbooru.GelbooruTagExtractor,
    "#count"   : 5,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=list&tags=meiya_neon",
    "#category": ("booru", "gelbooru", "tag"),
    "#class"   : gelbooru.GelbooruTagExtractor,
    "#pattern" : r"https://img\d\.gelbooru\.com/images/../../[0-9a-f]{32}\.jpg",
    "#range"   : "196-204",
    "#count"   : 9,
    "#sha1_url": "845a61aa1f90fb4ced841e8b7e62098be2e967bf",
},

{
    "#url"     : "https://gelbooru.com/index.php?page=pool&s=show&id=761",
    "#category": ("booru", "gelbooru", "pool"),
    "#class"   : gelbooru.GelbooruPoolExtractor,
    "#count"   : 6,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=favorites&s=view&id=279415",
    "#category": ("booru", "gelbooru", "favorite"),
    "#class"   : gelbooru.GelbooruFavoriteExtractor,
    "#count"   : 3,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=view&id=313638",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
    "#count"       : 1,
    "#sha1_content": "5e255713cbf0a8e0801dc423563c34d896bb9229",
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=view&id=313638",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?s=view&page=post&id=313638",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&id=313638&s=view",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?s=view&id=313638&page=post",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?id=313638&page=post&s=view",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?id=313638&s=view&page=post",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=view&id=6018318",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
    "#options"     : {"tags": True},
    "#sha1_content": "977caf22f27c72a5d07ea4d4d9719acdab810991",

    "tags_artist"   : "kirisaki_shuusei",
    "tags_character": str,
    "tags_copyright": "vocaloid",
    "tags_general"  : str,
    "tags_metadata" : str,
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=view&id=5938076",
    "#comment" : "video",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
    "#pattern"     : r"https://img\d\.gelbooru\.com/images/22/61/226111273615049235b001b381707bd0\.webm",
    "#sha1_content": "6360452fa8c2f0c1137749e81471238564df832a",
},

{
    "#url"     : "https://gelbooru.com/index.php?page=post&s=view&id=5997331",
    "#comment" : "notes",
    "#category": ("booru", "gelbooru", "post"),
    "#class"   : gelbooru.GelbooruPostExtractor,
    "#options" : {"notes": True},

    "notes": [
        {
            "body"  : "Look over this way when you talk~",
            "height": 553,
            "width" : 246,
            "x"     : 35,
            "y"     : 72,
        },
        {
            "body"  : """Hey~
Are you listening~?""",
            "height": 557,
            "width" : 246,
            "x"     : 1233,
            "y"     : 109,
        },
    ],
},

{
    "#url"     : "https://gelbooru.com/redirect.php?s=Ly9nZWxib29ydS5jb20vaW5kZXgucGhwP3BhZ2U9cG9zdCZzPXZpZXcmaWQ9MTgzMDA0Ng==",
    "#category": ("booru", "gelbooru", "redirect"),
    "#class"   : gelbooru.GelbooruRedirectExtractor,
    "#pattern" : r"https://gelbooru.com/index.php\?page=post&s=view&id=1830046",
},

)
