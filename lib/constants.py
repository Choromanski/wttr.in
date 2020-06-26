#vim: fileencoding=utf-8

WWO_CODE = {
    "113": "Sunny",
    "116": "PartlyCloudy",
    "119": "Cloudy",
    "122": "VeryCloudy",
    "143": "Fog",
    "176": "LightShowers",
    "179": "LightSleetShowers",
    "182": "LightSleet",
    "185": "LightSleet",
    "200": "ThunderyShowers",
    "227": "LightSnow",
    "230": "HeavySnow",
    "248": "Fog",
    "260": "Fog",
    "263": "LightShowers",
    "266": "LightRain",
    "281": "LightSleet",
    "284": "LightSleet",
    "293": "LightRain",
    "296": "LightRain",
    "299": "HeavyShowers",
    "302": "HeavyRain",
    "305": "HeavyShowers",
    "308": "HeavyRain",
    "311": "LightSleet",
    "314": "LightSleet",
    "317": "LightSleet",
    "320": "LightSnow",
    "323": "LightSnowShowers",
    "326": "LightSnowShowers",
    "329": "HeavySnow",
    "332": "HeavySnow",
    "335": "HeavySnowShowers",
    "338": "HeavySnow",
    "350": "LightSleet",
    "353": "LightShowers",
    "356": "HeavyShowers",
    "359": "HeavyRain",
    "362": "LightSleetShowers",
    "365": "LightSleetShowers",
    "368": "LightSnowShowers",
    "371": "HeavySnowShowers",
    "374": "LightSleetShowers",
    "377": "LightSleet",
    "386": "ThunderyShowers",
    "389": "ThunderyHeavyRain",
    "392": "ThunderySnowShowers",
    "395": "HeavySnowShowers",
}

WEATHER_SYMBOL = {
    "Unknown":             "✨",
    "Cloudy":              "☁️",
    "Fog":                 "🌫",
    "HeavyRain":           "🌧",
    "HeavyShowers":        "🌧",
    "HeavySnow":           "❄️",
    "HeavySnowShowers":    "❄️",
    "LightRain":           "🌦",
    "LightShowers":        "🌦",
    "LightSleet":          "🌧",
    "LightSleetShowers":   "🌧",
    "LightSnow":           "🌨",
    "LightSnowShowers":    "🌨",
    "PartlyCloudy":        "⛅️",
    "Sunny":               "☀️",
    "ThunderyHeavyRain":   "🌩",
    "ThunderyShowers":     "⛈",
    "ThunderySnowShowers": "⛈",
    "VeryCloudy": "☁️",
}

WEATHER_SYMBOL_WIDTH_VTE = {
    "✨": 2,
    "☁️": 1,
    "🌫": 2,
    "🌧": 2,
    "🌧": 2,
    "❄️": 1,
    "❄️": 1,
    "🌦": 1,
    "🌦": 1,
    "🌧": 1,
    "🌧": 1,
    "🌨": 2,
    "🌨": 2,
    "⛅️": 2,
    "☀️": 1,
    "🌩": 2,
    "⛈": 1,
    "⛈": 1,
    "☁️": 1,
}

WIND_DIRECTION = [
    "↓", "↙", "←", "↖", "↑", "↗", "→", "↘",
]

MOON_PHASES = (
    "🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"
)

WEATHER_SYMBOL_WI_DAY = {
    "Unknown":             "",
    "Cloudy":              "",
    "Fog":                 "",
    "HeavyRain":           "",
    "HeavyShowers":        "",
    "HeavySnow":           "",
    "HeavySnowShowers":    "",
    "LightRain":           "",
    "LightShowers":        "",
    "LightSleet":          "",
    "LightSleetShowers":   "",
    "LightSnow":           "",
    "LightSnowShowers":    "",
    "PartlyCloudy":        "",
    "Sunny":               "",
    "ThunderyHeavyRain":   "",
    "ThunderyShowers":     "",
    "ThunderySnowShowers": "",
    "VeryCloudy": "",
}

WEATHER_SYMBOL_WI_NIGHT = {
    "Unknown":             "",
    "Cloudy":              "",
    "Fog":                 "",
    "HeavyRain":           "",
    "HeavyShowers":        "",
    "HeavySnow":           "",
    "HeavySnowShowers":    "",
    "LightRain":           "",
    "LightShowers":        "",
    "LightSleet":          "",
    "LightSleetShowers":   "",
    "LightSnow":           "",
    "LightSnowShowers":    "",
    "PartlyCloudy":        "",
    "Sunny":               "",
    "ThunderyHeavyRain":   "",
    "ThunderyShowers":     "",
    "ThunderySnowShowers": "",
    "VeryCloudy": "",
}

WEATHER_SYMBOL_WIDTH_VTE_WI = {
}

WIND_DIRECTION_WI = [
    "", "", "", "", "", "", "", "",
]

WIND_SCALE_WI = [
    "", "", "", "", "", "", "", "", "", "", "", "", "",
]

MOON_PHASES_WI = (
    "", "", "", "", "", "", "",
    "", "", "", "", "", "", "",
    "", "", "", "", "", "", "",
    "", "", "", "", "", "", "",
)

WEATHER_SYMBOL_WEGO = {
    "Unknown": [
        "    .-.      ",
        "     __)     ",
        "    (        ",
        "     `-’     ",
        "      •      "],
    "Sunny": [
        "\033[38;5;226m    \\   /    \033[0m",
        "\033[38;5;226m     .-.     \033[0m",
        "\033[38;5;226m  ― (   ) ―  \033[0m",
        "\033[38;5;226m     `-’     \033[0m",
        "\033[38;5;226m    /   \\    \033[0m"],
    "PartlyCloudy": [
        "\033[38;5;226m   \\  /\033[0m      ",
        "\033[38;5;226m _ /\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m   \\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "             "],
    "Cloudy": [
        "             ",
        "\033[38;5;250m     .--.    \033[0m",
        "\033[38;5;250m  .-(    ).  \033[0m",
        "\033[38;5;250m (___.__)__) \033[0m",
        "             "],
    "VeryCloudy": [
        "             ",
        "\033[38;5;240;1m     .--.    \033[0m",
        "\033[38;5;240;1m  .-(    ).  \033[0m",
        "\033[38;5;240;1m (___.__)__) \033[0m",
        "             "],
    "LightShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ ‘ ‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    "HeavyShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;21;1m   ‚‘‚‘‚‘‚‘  \033[0m",
        "\033[38;5;21;1m   ‚’‚’‚’‚’  \033[0m"],
    "LightSnowShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *  *  * \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    "HeavySnowShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;240;1m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;240;1m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;240;1m(___(__) \033[0m",
        "\033[38;5;255;1m    * * * *  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m"],
    "LightSleetShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;111m     ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m* \033[0m",
        "\033[38;5;255m    *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘  \033[0m"],
    "ThunderyShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;228;5m    ⚡\033[38;5;111;25m‘ ‘\033[38;5;228;5m⚡\033[38;5;111;25m‘ ‘ \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m"],
    "ThunderyHeavyRain": [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘\033[38;5;228;5m⚡\033[38;5;21;25m‘‚\033[38;5;228;5m⚡\033[38;5;21;25m‚‘ \033[0m",
        "\033[38;5;21;1m  ‚’‚’\033[38;5;228;5m⚡\033[38;5;21;25m’‚’  \033[0m"],
    "ThunderySnowShowers": [
        "\033[38;5;226m _`/\"\"\033[38;5;250m.-.    \033[0m",
        "\033[38;5;226m  ,\\_\033[38;5;250m(   ).  \033[0m",
        "\033[38;5;226m   /\033[38;5;250m(___(__) \033[0m",
        "\033[38;5;255m     *\033[38;5;228;5m⚡\033[38;5;255;25m*\033[38;5;228;5m⚡\033[38;5;255;25m* \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m"],
    "LightRain": [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ ‘ ‘ ‘  \033[0m",
        "\033[38;5;111m   ‘ ‘ ‘ ‘   \033[0m"],
    "HeavyRain": [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;21;1m  ‚‘‚‘‚‘‚‘   \033[0m",
        "\033[38;5;21;1m  ‚’‚’‚’‚’   \033[0m"],
    "LightSnow": [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;255m    *  *  *  \033[0m",
        "\033[38;5;255m   *  *  *   \033[0m"],
    "HeavySnow": [
        "\033[38;5;240;1m     .-.     \033[0m",
        "\033[38;5;240;1m    (   ).   \033[0m",
        "\033[38;5;240;1m   (___(__)  \033[0m",
        "\033[38;5;255;1m   * * * *   \033[0m",
        "\033[38;5;255;1m  * * * *    \033[0m"],
    "LightSleet": [
        "\033[38;5;250m     .-.     \033[0m",
        "\033[38;5;250m    (   ).   \033[0m",
        "\033[38;5;250m   (___(__)  \033[0m",
        "\033[38;5;111m    ‘ \033[38;5;255m*\033[38;5;111m ‘ \033[38;5;255m*  \033[0m",
        "\033[38;5;255m   *\033[38;5;111m ‘ \033[38;5;255m*\033[38;5;111m ‘   \033[0m"],
    "Fog": [
        "             ",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "\033[38;5;251m  _ - _ - _  \033[0m",
        "\033[38;5;251m _ - _ - _ - \033[0m",
        "             "],
}

LOCALE = {
    "af": "af_ZA", "ar": "ar_TN", "az": "az_AZ", "be": "be_BY", "bg": "bg_BG",
    "bs": "bs_BA", "ca": "ca_ES", "cs": "cs_CZ", "cy": "cy_GB", "da": "da_DK",
    "de": "de_DE", "el": "el_GR", "eo": "eo", "es": "es_ES", "et": "et_EE",
    "fa": "fa_IR", "fi": "fi_FI", "fr": "fr_FR", "fy": "fy_NL", "ga": "ga_IE",
    "he": "he_IL", "hr": "hr_HR", "hu": "hu_HU", "hy": "hy_AM", "ia": "ia",
    "id": "id_ID", "is": "is_IS", "it": "it_IT", "ja": "ja_JP", "jv": "en_US",
    "ka": "ka_GE", "ko": "ko_KR", "kk": "kk_KZ", "ky": "ky_KG", "lt": "lt_LT",
    "lv": "lv_LV", "mk": "mk_MK", "ml": "ml_IN", "nb": "nb_NO", "nl": "nl_NL",
    "nn": "nn_NO", "pt": "pt_PT", "pt-br":"pt_BR", "pl": "pl_PL", "ro": "ro_RO",
    "ru": "ru_RU", "sv": "sv_SE", "sk": "sk_SK", "sl": "sl_SI", "sr": "sr_RS",
    "sr-lat": "sr_RS@latin", "sw": "sw_KE", "th": "th_TH", "tr": "tr_TR", "uk": "uk_UA",
    "uz": "uz_UZ", "vi": "vi_VN", "zh": "zh_TW", "zu": "zu_ZA",
}
