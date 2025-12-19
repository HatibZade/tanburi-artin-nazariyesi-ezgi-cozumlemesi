# -*- coding: utf-8 -*-
"""Tanburi Küçük Artin veri seti (stable, locked).

Kullanım:
    from data.tanburi_kucuk_artin_data import DATA
"""

DATA = {
  "source": {
    "nazariyeci": "Tanburi Küçük Artin",
    "work": "Musiki Edvarı (18. yy)",
    "edition": "Eugenia Popescu-Judetz (ed.), Tanburi Küçük Artin: A Musical Treatise of the Eighteenth Century, Pan Yayınları, 2002"
  },
  "schema_version": "clean-locked-1",
  "generation": {
    "from_pdf": "Tanburi Küçük Artin a musical treatise of the eighteenth century 0-59_.pdf",
    "method": "Regex + OCR-artifact cleanup over 'bir mızrab' seyir dizileri",
    "entry_count": 74
  },
  "notes": [
    "Bu paket 'stable' dosya adları kullanır; GitHub/Streamlit tarafında sürüm karışıklığı yaşanmaz.",
    "kullanilan_perdeler: asil_perdeler/nim_perdeler ayrımı ASIL_MAP sözlüğüne göre kilitlenmiştir (Dügâh/dugah/Dügâh yazım farkları sorun çıkarmaz).",
    "Âgâz/Merkez/Karar/Alt-Üst alanları Artin metninde sistematik başlıklar halinde verilmediğinden seyir dizilerinden türetilmiştir."
  ],
  "rank_order_used": [
    "Yegah",
    "Aşiran",
    "Rast",
    "Dügah",
    "Segah",
    "Çargah",
    "Neva",
    "Hüseyni",
    "Acem",
    "Gerdaniye",
    "Muhayyer",
    "Tiz Çargah",
    "Tiz Segah"
  ],
  "makamlar": [
    {
      "id": "rehavi",
      "name_tr": "Rehavi",
      "evidence": {
        "page_start": 29,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Yegah",
          "Rast",
          "Bir mız rab dügah",
          "Nihavend",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Yegah",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast",
            "Yegah"
          ],
          "nim_perdeler": [
            "Bir mız rab dügah",
            "Nihavend"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "pencgah",
      "name_tr": "Pençgah",
      "evidence": {
        "page_start": 29,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Buselik",
          "Bir mız rab hicaz",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Neva",
          "Hicaz",
          "Buselik",
          "Dügah",
          "Bir nıızrab rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Bir nıızrab rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Dügah"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Buselik",
            "Bir mız rab hicaz",
            "Eviç",
            "Bir nıızrab rast"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "nikriz",
      "name_tr": "Nikriz",
      "evidence": {
        "page_start": 29,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "nihavend_i_sagir",
      "name_tr": "nihavend-i sagir",
      "evidence": {
        "page_start": 29,
        "seyir_sequence": [
          "Saha",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Nihavend",
          "Çargah",
          "Saba",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Saha",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Saha",
            "Nihavend",
            "Saba"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "nihavend",
      "name_tr": "nihavend",
      "evidence": {
        "page_start": 30,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Beyati",
          "Neva",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Hüseyni",
          "Mahur",
          "Gerdaniye",
          "Mahur",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Dügah",
            "Hüseyni",
            "Gerdaniye",
            "Rast"
          ],
          "nim_perdeler": [
            "Beyati",
            "Nihavend",
            "Mahur",
            "Buselik"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Hüseynî",
            "Gerdâniye",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "rekb",
      "name_tr": "Rekb",
      "evidence": {
        "page_start": 30,
        "seyir_sequence": [
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Buselik",
          "Çargah",
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Geveşt",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Nihavend",
          "Çargah",
          "Saba",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Geveşt",
          "Aşiran",
          "Yegah",
          "Bir ıııız rab aşiran",
          "Geveşt",
          "Rast",
          "Dügah",
          "Mahur",
          "Gerdaniye",
          "Muhayyer",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Malıur",
          "Neva",
          "Lıicaz",
          "Dügah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Geveşt",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Dügah",
            "Rast",
            "Hüseyni",
            "Aşiran",
            "Yegah",
            "Gerdaniye",
            "Muhayyer"
          ],
          "nim_perdeler": [
            "Beyati",
            "Buselik",
            "Geveşt",
            "Nihavend",
            "Saba",
            "Acem",
            "Bir ıııız rab aşiran",
            "Mahur",
            "Sünbüle",
            "Malıur",
            "Lıicaz"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast",
            "Hüseynî",
            "Aşîrân",
            "Yegâh",
            "Gerdâniye",
            "Muhayyer"
          ]
        }
      }
    },
    {
      "id": "ziretkend_i_rumi",
      "name_tr": "Ziretkend-i rumi",
      "evidence": {
        "page_start": 31,
        "seyir_sequence": [
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Geveşt",
          "Buselik",
          "Segah",
          "Zirgüle",
          "Rast",
          "Segah",
          "Buse lik",
          "Eviç",
          "Mahur",
          "Eviç",
          "Beyati",
          "Neva",
          "Buselik",
          "Segah",
          "Zirgüle",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Gerdaniye",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Buselik",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Muhayyer",
            "Neva",
            "Çargah",
            "Dügah",
            "Segah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem",
            "Buselik",
            "Geveşt",
            "Zirgüle",
            "Buse lik",
            "Eviç",
            "Mahur",
            "Beyati"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Muhayyer",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Segâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muberka_i_rumi",
      "name_tr": "Müberka-i rumi",
      "evidence": {
        "page_start": 32,
        "seyir_sequence": [
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Acemaşiran",
          "Aşiran",
          "Rast",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Rast",
          "Aşiran",
          "Arak",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Aşiran",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Dügah",
            "Rast",
            "Aşiran",
            "Segah"
          ],
          "nim_perdeler": [
            "Beyati",
            "Nihavend",
            "Acemaşiran",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast",
            "Aşîrân",
            "Segâh"
          ]
        }
      }
    },
    {
      "id": "hicaz_buzurk",
      "name_tr": "Hicaz-büzürk",
      "evidence": {
        "page_start": 32,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Segah",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Aşiranın yegah",
          "Arak",
          "Rast",
          "Dügah",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Arak",
            "Aşiranın yegah"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "nihavend_i_rumi",
      "name_tr": "nihavend-i rumi",
      "evidence": {
        "page_start": 32,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Nihavend i dügah",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Rast",
          "Geveşt",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Nihavend i dügah",
            "Nihavend",
            "Geveşt"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muberka",
      "name_tr": "Müberka",
      "evidence": {
        "page_start": 32,
        "seyir_sequence": [
          "Rast",
          "Geveşt",
          "Aşiran",
          "Yegah",
          "Aşiran",
          "Geveşt",
          "Rast",
          "Dügah",
          "Segah",
          "Rast",
          "Dügah",
          "Geveşt",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Rast",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Segah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Rast",
            "Aşiran",
            "Yegah",
            "Dügah",
            "Segah"
          ],
          "nim_perdeler": [
            "Geveşt"
          ],
          "asil_perde_canonical": [
            "Rast",
            "Aşîrân",
            "Yegâh",
            "Dügâh",
            "Segâh"
          ]
        }
      }
    },
    {
      "id": "mahurek",
      "name_tr": "Mahurek",
      "evidence": {
        "page_start": 33,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Dügah",
          "Buse lik",
          "Dügah",
          "Rast",
          "Geveşt",
          "Rast"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Rast",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Buselik",
            "Buse lik",
            "Geveşt"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "rast",
      "name_tr": "Rast",
      "evidence": {
        "page_start": 33,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Segah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muhayyer",
      "name_tr": "Muhayyer",
      "evidence": {
        "page_start": 33,
        "seyir_sequence": [
          "Tiz çargah",
          "Tiz segah",
          "Muhayyer",
          "Tiz segah",
          "Mu hayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Çargah",
          "Saha",
          "Segah",
          "Dügah",
          "Segah",
          "Çargah",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah",
          "Saha",
          "Dügah",
          "Segah",
          "Çargah",
          "Saba",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Tiz çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Tiz çargah",
            "Tiz segah",
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Mu hayyer",
            "Eviç",
            "Saha",
            "Saba"
          ],
          "asil_perde_canonical": [
            "Tiz Çargâh",
            "Tiz Segâh",
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "dugah_i_rumi",
      "name_tr": "Dügah-i rumi",
      "evidence": {
        "page_start": 33,
        "seyir_sequence": [
          "Dügah",
          "Zirgüle",
          "Dügah",
          "Segah",
          "Çargah",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Zirgüle",
          "Segah",
          "Buselik",
          "Segah",
          "Dügah",
          "Zirgü le",
          "Buselik",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Dügah",
            "Segah",
            "Çargah"
          ],
          "nim_perdeler": [
            "Zirgüle",
            "Saha",
            "Arak",
            "Buselik",
            "Zirgü le"
          ],
          "asil_perde_canonical": [
            "Dügâh",
            "Segâh",
            "Çargâh"
          ]
        }
      }
    },
    {
      "id": "sunbule",
      "name_tr": "Sünbüle",
      "evidence": {
        "page_start": 34,
        "seyir_sequence": [
          "Muhayyer",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Saba",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Çargah",
          "Saha",
          "Çargah",
          "Segah",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Kürdi",
          "Çargah",
          "Saba",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Muhayyer",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Sünbüle",
            "Acem",
            "Saba",
            "Saha",
            "Kürdi"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muhayyer_buselik",
      "name_tr": "Muhayyer-buselik",
      "evidence": {
        "page_start": 34,
        "seyir_sequence": [
          "Tiz çargah",
          "Tiz segah",
          "Muhayyer",
          "Tiz segah",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Çargah",
          "Buselik",
          "Tiz neva",
          "Tiz çargah",
          "Sünbüle",
          "Mu hayyer",
          "Gerdaniye",
          "Mahur",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Çargah",
          "Buselik",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Tiz çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Tiz çargah",
            "Tiz segah",
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast",
            "Tiz neva"
          ],
          "nim_perdeler": [
            "Eviç",
            "Buselik",
            "Sünbüle",
            "Mu hayyer",
            "Mahur",
            "Acem",
            "Zirgüle"
          ],
          "asil_perde_canonical": [
            "Tiz Çargâh",
            "Tiz Segâh",
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast",
            "Tiz Nevâ"
          ]
        }
      }
    },
    {
      "id": "zemzeme",
      "name_tr": "Zemzeme",
      "evidence": {
        "page_start": 35,
        "seyir_sequence": [
          "Acem",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Dügah",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "hisar",
      "name_tr": "Hisar",
      "evidence": {
        "page_start": 35,
        "seyir_sequence": [
          "Acem",
          "Hüseyni",
          "Hisar",
          "Çargah",
          "Hüseyni",
          "Eviç",
          "Şehnaz",
          "Muhayyer",
          "Tiz segah",
          "Muhayyer",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Hisar",
          "Çargah",
          "Segah",
          "Dügah",
          "Saba",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Çargah",
            "Muhayyer",
            "Tiz segah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Acem",
            "Hisar",
            "Eviç",
            "Şehnaz",
            "Saba"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Çargâh",
            "Muhayyer",
            "Tiz Segâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "kucek",
      "name_tr": "Küçek",
      "evidence": {
        "page_start": 35,
        "seyir_sequence": [
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Gerdaniye",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Eviç",
            "Acem"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "isfahanek",
      "name_tr": "Isfahanek",
      "evidence": {
        "page_start": 36,
        "seyir_sequence": [
          "Tiz çargalı",
          "Tiz buselik",
          "Muhayyer",
          "Şehnaz",
          "Gerda niye",
          "Eviç",
          "Şehnaz",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Saha",
          "Çargah",
          "Segah",
          "Saha",
          "Çargah",
          "Segah",
          "Segah",
          "Çargalı",
          "Saha",
          "Çargah",
          "Segah",
          "Hüseyni",
          "Saha",
          "Çargalı",
          "Segalı",
          "Dügalı",
          "Geveşt",
          "Rast",
          "Neva",
          "Hicaz",
          "Segalı",
          "Hicaz",
          "Segalı",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Tiz çargalı",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Saha",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Çargah",
            "Segah",
            "Rast",
            "Neva",
            "Dügah"
          ],
          "nim_perdeler": [
            "Tiz çargalı",
            "Tiz buselik",
            "Şehnaz",
            "Gerda niye",
            "Eviç",
            "Saha",
            "Çargalı",
            "Segalı",
            "Dügalı",
            "Geveşt",
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Çargâh",
            "Segâh",
            "Rast",
            "Nevâ",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "sipihr",
      "name_tr": "Sipihr",
      "evidence": {
        "page_start": 36,
        "seyir_sequence": [
          "Çargah",
          "Saha",
          "Çargah",
          "Dügah",
          "Segah",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Zirgüle",
          "Dügah",
          "Segah",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Dügah",
            "Segah",
            "Gerdaniye",
            "Hüseyni",
            "Neva"
          ],
          "nim_perdeler": [
            "Saha",
            "Acem",
            "Zirgüle",
            "Arak",
            "Hicaz",
            "Nihavend"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Dügâh",
            "Segâh",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ"
          ]
        }
      }
    },
    {
      "id": "dugal",
      "name_tr": "Dügalı",
      "evidence": {
        "page_start": 36,
        "seyir_sequence": [
          "Dügah",
          "Arak",
          "Rast",
          "Dügalı",
          "Segalı",
          "Çargalı",
          "Ne va",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargalı",
          "Segalı",
          "Dügalı",
          "Arak",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Dügah",
            "Rast",
            "Hüseyni",
            "Gerdaniye",
            "Neva"
          ],
          "nim_perdeler": [
            "Arak",
            "Dügalı",
            "Segalı",
            "Çargalı",
            "Ne va",
            "Eviç"
          ],
          "asil_perde_canonical": [
            "Dügâh",
            "Rast",
            "Hüseynî",
            "Gerdâniye",
            "Nevâ"
          ]
        }
      }
    },
    {
      "id": "hisarek",
      "name_tr": "Hisarek",
      "evidence": {
        "page_start": 37,
        "seyir_sequence": [
          "Muhayyer",
          "Şehnaz",
          "Mahur",
          "Hüseyni",
          "Hisar",
          "Çargah",
          "Buselik"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Muhayyer",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Muhayyer",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Buselik",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Hüseyni",
            "Çargah"
          ],
          "nim_perdeler": [
            "Şehnaz",
            "Mahur",
            "Hisar",
            "Buselik"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Hüseynî",
            "Çargâh"
          ]
        }
      }
    },
    {
      "id": "hicaz",
      "name_tr": "Hicaz",
      "evidence": {
        "page_start": 37,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Segah",
            "Dügah",
            "Rast",
            "Hüseyni"
          ],
          "nim_perdeler": [
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Segâh",
            "Dügâh",
            "Rast",
            "Hüseynî"
          ]
        }
      }
    },
    {
      "id": "sehnaz",
      "name_tr": "Şehnaz",
      "evidence": {
        "page_start": 37,
        "seyir_sequence": [
          "Muhayyer",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Muhayyer",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Hüseyni",
            "Neva",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Şehnaz",
            "Eviç",
            "Hicaz",
            "Zirgüle"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Hüseynî",
            "Nevâ",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "u_zzal",
      "name_tr": "U zzal",
      "evidence": {
        "page_start": 37,
        "seyir_sequence": [
          "Hüseyiıi",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Hicaz",
          "Dügah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyiıi",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Eviç",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Hüseyiıi",
            "Eviç",
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "zirgule",
      "name_tr": "Zirgüle",
      "evidence": {
        "page_start": 37,
        "seyir_sequence": [
          "Dügah",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Zirgüle",
          "Dügah",
          "Segah",
          "Hicaz",
          "Segah",
          "Hicaz",
          "Segah",
          "Dügah",
          "Aşiran",
          "Dü gah",
          "Aşiran"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Aşiran",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Aşiran",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Dügah",
            "Hüseyni",
            "Neva",
            "Segah",
            "Aşiran"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Zirgüle",
            "Arak",
            "Dü gah"
          ],
          "asil_perde_canonical": [
            "Dügâh",
            "Hüseynî",
            "Nevâ",
            "Segâh",
            "Aşîrân"
          ]
        }
      }
    },
    {
      "id": "hunayun",
      "name_tr": "Hünıayun",
      "evidence": {
        "page_start": 38,
        "seyir_sequence": [
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Hicaz",
          "Segah",
          "Dügah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Rast",
          "Dügah",
          "Segah",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Dügah",
          "Zir güle",
          "Saha",
          "Çargah",
          "Segah",
          "Segah",
          "Gerdaniye",
          "Mahur",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Segah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Gerdaniye",
            "Segah",
            "Dügah",
            "Rast",
            "Çargah"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Acem",
            "Arak",
            "Zir güle",
            "Saha",
            "Mahur",
            "Beyati"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Gerdâniye",
            "Segâh",
            "Dügâh",
            "Rast",
            "Çargâh"
          ]
        }
      }
    },
    {
      "id": "suzidil",
      "name_tr": "Suzidil",
      "evidence": {
        "page_start": 38,
        "seyir_sequence": [
          "Muhayyer",
          "Şehnaz",
          "Acem",
          "Hüseyni",
          "Acem",
          "Şehnaz",
          "Muhayyer",
          "Sünbüle",
          "Muhayyer",
          "Şehnaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Nihavend",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Zirgüle",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hi caz",
          "Segah",
          "Dügilli",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Bu selik",
          "Dügah",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Saba",
          "Çargah",
          "Segilli",
          "Nihavend",
          "Segah",
          "Hüseyni",
          "Saha",
          "Çargah",
          "Hüseyni",
          "Saha",
          "Çargah",
          "Segah",
          "Nihavend",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Muhayyer",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Hüseyni",
            "Neva",
            "Dügah",
            "Segah",
            "Gerdaniye",
            "Çargah",
            "Rast"
          ],
          "nim_perdeler": [
            "Şehnaz",
            "Acem",
            "Sünbüle",
            "Hicaz",
            "Nihavend",
            "Zirgüle",
            "Eviç",
            "Hi caz",
            "Dügilli",
            "Bu selik",
            "Buselik",
            "Saba",
            "Segilli",
            "Saha"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Hüseynî",
            "Nevâ",
            "Dügâh",
            "Segâh",
            "Gerdâniye",
            "Çargâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muhalifek_segah",
      "name_tr": "Muhalifek-segah",
      "evidence": {
        "page_start": 39,
        "seyir_sequence": [
          "Eviç",
          "Acem",
          "Neva",
          "Hicaz",
          "Segah",
          "Nihavend",
          "Segah",
          "Hicaz",
          "Neva",
          "Muhayyer",
          "Şehnaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segilli",
          "Ni havend",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Eviç",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Segah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Segah",
            "Muhayyer",
            "Hüseyni"
          ],
          "nim_perdeler": [
            "Eviç",
            "Acem",
            "Hicaz",
            "Nihavend",
            "Şehnaz",
            "Segilli",
            "Ni havend"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Segâh",
            "Muhayyer",
            "Hüseynî"
          ]
        }
      }
    },
    {
      "id": "huzzam_i_rumi",
      "name_tr": "Hüzzam-i rumi",
      "evidence": {
        "page_start": 40,
        "seyir_sequence": [
          "Segah",
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Ni havend",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Nihavend",
          "Nihavend",
          "Segah",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Segah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Segah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Segah",
            "Neva",
            "Çargah",
            "Hüseyni"
          ],
          "nim_perdeler": [
            "Beyati",
            "Ni havend",
            "Nihavend",
            "Acem"
          ],
          "asil_perde_canonical": [
            "Segâh",
            "Nevâ",
            "Çargâh",
            "Hüseynî"
          ]
        }
      }
    },
    {
      "id": "karcgar",
      "name_tr": "Karcığar",
      "evidence": {
        "page_start": 40,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Segah",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Neva",
          "Hicaz",
          "Segah",
          "Nihavend",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Segah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Segah",
            "Hüseyni"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Nihavend"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Segâh",
            "Hüseynî"
          ]
        }
      }
    },
    {
      "id": "gevest",
      "name_tr": "Geveşt",
      "evidence": {
        "page_start": 40,
        "seyir_sequence": [
          "Segah",
          "Saha",
          "Çargah",
          "Segah",
          "Nihavend",
          "Rast",
          "Geveşt",
          "Rast",
          "Geveşt",
          "Rast",
          "Geveşt",
          "Aşiran",
          "Rast",
          "Geveşt",
          "Aşiran",
          "Yegah",
          "Çargah",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Segah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Segah",
            "Çargah",
            "Rast",
            "Aşiran",
            "Yegah"
          ],
          "nim_perdeler": [
            "Saha",
            "Nihavend",
            "Geveşt"
          ],
          "asil_perde_canonical": [
            "Segâh",
            "Çargâh",
            "Rast",
            "Aşîrân",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "segah",
      "name_tr": "Segah",
      "evidence": {
        "page_start": 40,
        "seyir_sequence": [
          "Segah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Çargah",
          "Neva",
          "Segah",
          "Çargah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Segah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Segah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Segah",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [],
          "asil_perde_canonical": [
            "Segâh",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "acem",
      "name_tr": "Acem",
      "evidence": {
        "page_start": 41,
        "seyir_sequence": [
          "Acem",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Acem",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Acem"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "isfahan",
      "name_tr": "Isfahan",
      "evidence": {
        "page_start": 41,
        "seyir_sequence": [
          "Neva",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Rieva",
          "Hicaz",
          "Muhayyer",
          "Şehnaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Çargah",
          "Segah",
          "Çargah",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Muhayyer",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Buselik",
            "Hicaz",
            "Acem",
            "Rieva",
            "Şehnaz",
            "Saha"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Muhayyer",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "nisabur",
      "name_tr": "Nişabur",
      "evidence": {
        "page_start": 41,
        "seyir_sequence": [
          "Muhayyer",
          "Gerdaniye",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Dügah",
          "Nihavend",
          "Çargah",
          "Neva",
          "Çargah",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hü seyni",
          "Çargah",
          "Inuhayyer",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Kürdi",
          "Çargah",
          "Neva",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Muhayyer",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Sünbüle",
            "Acem",
            "Hicaz",
            "Nihavend",
            "Eviç",
            "Hü seyni",
            "Inuhayyer",
            "Kürdi"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "mustear",
      "name_tr": "Müstear",
      "evidence": {
        "page_start": 42,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Hicaz",
          "Segah",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Dügah",
          "Segah",
          "Çargah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Segah",
            "Hüseyni",
            "Dügah"
          ],
          "nim_perdeler": [
            "Acem",
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Hüseynî",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "acemasiran",
      "name_tr": "Acemaşiran",
      "evidence": {
        "page_start": 43,
        "seyir_sequence": [
          "Acem",
          "Muhayyer",
          "Gerdaniye",
          "Acem",
          "Hü seyni",
          "Neva",
          "Çargah",
          "Dügah",
          "Neva",
          "Dügah",
          "Rast",
          "Acemaşiran",
          "Yegah",
          "Aşiran",
          "Acemaşiran"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Acem",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Acemaşiran",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast",
            "Yegah",
            "Aşiran"
          ],
          "nim_perdeler": [
            "Acem",
            "Hü seyni",
            "Acemaşiran"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast",
            "Yegâh",
            "Aşîrân"
          ]
        }
      }
    },
    {
      "id": "nisaburek",
      "name_tr": "Nişaburek",
      "evidence": {
        "page_start": 43,
        "seyir_sequence": [
          "Neva",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hic az",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Buselik",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Dügah"
          ],
          "nim_perdeler": [
            "Buselik",
            "Hicaz",
            "Hic az"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "huzzam",
      "name_tr": "Hüzzam",
      "evidence": {
        "page_start": 43,
        "seyir_sequence": [
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Acem",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Gerdaniye",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Acem",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Hicaz",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Neva"
          ],
          "nim_perdeler": [
            "Acem",
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Nevâ"
          ]
        }
      }
    },
    {
      "id": "ye_gah",
      "name_tr": "Ye gah",
      "evidence": {
        "page_start": 43,
        "seyir_sequence": [
          "Ne va",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Ara k",
          "Aşiran",
          "Rast",
          "Arak",
          "Aşiran",
          "Yegah",
          "Arak",
          "Aşiran",
          "Arak",
          "Yegah",
          "Pes hicaz",
          "Yegah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Ne va",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Aşiran",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Yegah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Segah",
            "Dügah",
            "Rast",
            "Aşiran",
            "Yegah"
          ],
          "nim_perdeler": [
            "Ne va",
            "Ara k",
            "Arak",
            "Pes hicaz"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast",
            "Aşîrân",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "nihavendinek",
      "name_tr": "nihavendinek",
      "evidence": {
        "page_start": 43,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Muhayyer",
          "Şehnaz",
          "Aceın",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Rast",
          "Geveşt",
          "Şorizen",
          "Rast",
          "Arak",
          "Şorizen",
          "Yegah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Yegah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Dügah",
            "Muhayyer",
            "Hüseyni",
            "Rast",
            "Yegah"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Nihavend",
            "Şehnaz",
            "Aceın",
            "Geveşt",
            "Şorizen",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Dügâh",
            "Muhayyer",
            "Hüseynî",
            "Rast",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "beyati",
      "name_tr": "Beyati",
      "evidence": {
        "page_start": 44,
        "seyir_sequence": [
          "Segah",
          "Çargah",
          "Neva",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Dügah",
          "Segah",
          "Neva",
          "Çargah",
          "Segah",
          "Saba",
          "Çargah",
          "Segah",
          "Dügah",
          "Zir güle",
          "Arak",
          "Dügah",
          "Zirgüle",
          "Rast",
          "Arak",
          "Çargah",
          "Dügah",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Segah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Segah",
            "Çargah",
            "Neva",
            "Hüseyni",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem",
            "Saba",
            "Zir güle",
            "Arak",
            "Zirgüle"
          ],
          "asil_perde_canonical": [
            "Segâh",
            "Çargâh",
            "Nevâ",
            "Hüseynî",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "ussak",
      "name_tr": "Uşşak",
      "evidence": {
        "page_start": 44,
        "seyir_sequence": [
          "Geveşt",
          "Rast",
          "Dügah",
          "Rast",
          "Dügah",
          "Rast",
          "Dügah",
          "Geveşt",
          "Rast",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Geveşt",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Rast",
            "Dügah",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah"
          ],
          "nim_perdeler": [
            "Geveşt",
            "Acem"
          ],
          "asil_perde_canonical": [
            "Rast",
            "Dügâh",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh"
          ]
        }
      }
    },
    {
      "id": "mustear_i_rumi",
      "name_tr": "Müstear-i rumi",
      "evidence": {
        "page_start": 44,
        "seyir_sequence": [
          "Neva",
          "Beyati",
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Neva",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Beyati"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "nevruz_i_acem",
      "name_tr": "Nevruz-i acem",
      "evidence": {
        "page_start": 45,
        "seyir_sequence": [
          "Acem",
          "Gerdaııiye",
          "Acem",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Sa ba",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Çargah",
          "Neva",
          "Beyati",
          "Neva",
          "Gerdaniye",
          "Mahur",
          "Beyati",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Rast",
          "Geveşt",
          "Şorizen",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Çargah",
          "Neva",
          "Beyati",
          "Neva",
          "Gerdaııiye",
          "Mahur",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem",
            "Gerdaııiye",
            "Beyati",
            "Sa ba",
            "Mahur",
            "Hicaz",
            "Nihavend",
            "Geveşt",
            "Şorizen"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "arahan",
      "name_tr": "Arahan",
      "evidence": {
        "page_start": 45,
        "seyir_sequence": [
          "Neva",
          "Hicaz",
          "Neva",
          "Beyati",
          "Mahur",
          "Gerdaniye",
          "Mu hayyer",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Mahur",
          "Beyati",
          "Neva",
          "Hicaz",
          "Nihavend",
          "Dügah",
          "Rast",
          "Geveşt",
          "Şorizen",
          "Rast",
          "Geveşt",
          "Şorizen",
          "Yegah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Yegah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Gerdaniye",
            "Muhayyer",
            "Dügah",
            "Rast",
            "Yegah"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Beyati",
            "Mahur",
            "Mu hayyer",
            "Sünbüle",
            "Nihavend",
            "Geveşt",
            "Şorizen"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Gerdâniye",
            "Muhayyer",
            "Dügâh",
            "Rast",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "huzi",
      "name_tr": "Hüzi",
      "evidence": {
        "page_start": 46,
        "seyir_sequence": [
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Rast",
          "Dügah",
          "Segah",
          "Çargah",
          "Segah",
          "Segah",
          "Rast",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Çargah",
          "Segah",
          "Dügah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Aşiran",
          "Arak",
          "Rast",
          "Arak",
          "Aşiran",
          "Yegah",
          "Segah",
          "Çargah",
          "Neva",
          "Hü seyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Rast",
          "Arak",
          "Aşiran"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Segah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Aşiran",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast",
            "Hüseyni",
            "Aşiran",
            "Yegah"
          ],
          "nim_perdeler": [
            "Buselik",
            "Hicaz",
            "Acem",
            "Arak",
            "Hü seyni"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast",
            "Hüseynî",
            "Aşîrân",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "n_eva",
      "name_tr": "N eva",
      "evidence": {
        "page_start": 46,
        "seyir_sequence": [
          "Neva",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Çargah",
          "Gerdaniye",
          "Muhayyer",
          "Tiz çargah",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Beya ti",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Geveşt",
          "Rast",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Dügah",
          "Segah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Segah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Gerdaniye",
            "Hüseyni",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast",
            "Muhayyer",
            "Tiz çargah"
          ],
          "nim_perdeler": [
            "Eviç",
            "Sünbüle",
            "Beya ti",
            "Geveşt"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Gerdâniye",
            "Hüseynî",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast",
            "Muhayyer",
            "Tiz Çargâh"
          ]
        }
      }
    },
    {
      "id": "buselik",
      "name_tr": "Buselik",
      "evidence": {
        "page_start": 47,
        "seyir_sequence": [
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Dügah",
          "Buselik",
          "Çargah",
          "Dügah",
          "Buselik",
          "Rast",
          "Hisar",
          "Çargah",
          "Buselik",
          "Çargah",
          "Dügah",
          "Buselik",
          "Rast",
          "Hisar",
          "Çargah",
          "Buselik",
          "Muhay yer",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Hisar",
          "Çargah",
          "Buselik",
          "Dügah",
          "Zirgüle",
          "Çargah",
          "Bu selik",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem",
            "Buselik",
            "Hisar",
            "Muhay yer",
            "Şehnaz",
            "Eviç",
            "Zirgüle",
            "Bu selik"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "suzinak",
      "name_tr": "Suzinak",
      "evidence": {
        "page_start": 48,
        "seyir_sequence": [
          "Hüseyni",
          "Hisar",
          "Muhayyer",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Hisar",
          "Çargah",
          "Buselik",
          "Dügah",
          "Zirgüle",
          "Zirgüle",
          "Dügah",
          "Buselik",
          "Çargah",
          "Buse lik",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Dügah",
          "Zirgüle",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Zirgüle",
          "Arak",
          "Hisar",
          "Hüseyni",
          "Mahur",
          "Gerdaniye",
          "Mu hayyer",
          "Sünbüle",
          "Muhayyer",
          "Gerdaniye",
          "Mahur",
          "Hüseyni",
          "Hisar",
          "Hicaz",
          "Hicaz",
          "Hisar",
          "Hüseyni",
          "Hisar",
          "Hicaz",
          "Segah",
          "Hicaz",
          "Segah",
          "Neva",
          "Hüseyni",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Hüseyni",
          "Saba",
          "Çargah",
          "Segah",
          "Saba",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Muhayyer",
            "Çargah",
            "Dügah",
            "Gerdaniye",
            "Segah",
            "Neva"
          ],
          "nim_perdeler": [
            "Hisar",
            "Şehnaz",
            "Eviç",
            "Buselik",
            "Zirgüle",
            "Buse lik",
            "Arak",
            "Mahur",
            "Mu hayyer",
            "Sünbüle",
            "Hicaz",
            "Saba"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Muhayyer",
            "Çargâh",
            "Dügâh",
            "Gerdâniye",
            "Segâh",
            "Nevâ"
          ]
        }
      }
    },
    {
      "id": "nevruz_i_rumi",
      "name_tr": "Nevruz-i rumi",
      "evidence": {
        "page_start": 49,
        "seyir_sequence": [
          "Hüseyni",
          "Hisar",
          "Hicaz",
          "Hicaz",
          "Beyati",
          "Hüseyni",
          "Hisar",
          "Hicaz",
          "Segah",
          "Dügah",
          "Dügah",
          "Segah",
          "Hicaz",
          "Dügah",
          "Segah",
          "Zirgüle",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Muhay yer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Ne va",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Dügah",
          "Buselik",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Arak",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüsey ni",
          "Neva",
          "Hicaz",
          "Segah",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Arak",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Segah",
            "Dügah",
            "Gerdaniye",
            "Neva",
            "Rast",
            "Çargah",
            "Muhayyer"
          ],
          "nim_perdeler": [
            "Hisar",
            "Hicaz",
            "Beyati",
            "Zirgüle",
            "Eviç",
            "Muhay yer",
            "Ne va",
            "Acem",
            "Buselik",
            "Arak",
            "Hüsey ni"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Segâh",
            "Dügâh",
            "Gerdâniye",
            "Nevâ",
            "Rast",
            "Çargâh",
            "Muhayyer"
          ]
        }
      }
    },
    {
      "id": "selrnek",
      "name_tr": "Selrnek",
      "evidence": {
        "page_start": 50,
        "seyir_sequence": [
          "Hüseyni",
          "Muhayyer",
          "Hüseyni",
          "Muhayyer",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Neva",
          "Dügah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Muhayyer",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [],
          "asil_perde_canonical": [
            "Hüseynî",
            "Muhayyer",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "huseyni_kurdi",
      "name_tr": "Hüseyni-kürdi",
      "evidence": {
        "page_start": 50,
        "seyir_sequence": [
          "Çargah",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Dügah",
          "Kürdi",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Neva",
            "Hüseyni",
            "Gerdaniye",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Eviç",
            "Kürdi"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Nevâ",
            "Hüseynî",
            "Gerdâniye",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "asiran_kurdi",
      "name_tr": "Aşiran-kürdi",
      "evidence": {
        "page_start": 50,
        "seyir_sequence": [
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Dügah",
          "Kürdi",
          "Çargah",
          "Kürdi",
          "Dügah",
          "Rast",
          "Acemaşiran",
          "Aşiran",
          "Aşiran",
          "Acemaşiran",
          "Rast",
          "Acemaşiran",
          "Aşiran",
          "Yegah",
          "Muhayyer",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Dügah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Arak",
          "Rast",
          "Arak",
          "Aşiran"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Hüseyni",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Aşiran",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Neva",
            "Gerdaniye",
            "Çargah",
            "Dügah",
            "Rast",
            "Aşiran",
            "Yegah",
            "Muhayyer",
            "Segah"
          ],
          "nim_perdeler": [
            "Eviç",
            "Kürdi",
            "Acemaşiran",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Nevâ",
            "Gerdâniye",
            "Çargâh",
            "Dügâh",
            "Rast",
            "Aşîrân",
            "Yegâh",
            "Muhayyer",
            "Segâh"
          ]
        }
      }
    },
    {
      "id": "asiranek",
      "name_tr": "Aşiranek",
      "evidence": {
        "page_start": 51,
        "seyir_sequence": [
          "Arak",
          "Zirgüle",
          "Dügah",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Buselik",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hi caz",
          "Buselik",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Dügah",
          "Zirgüle",
          "Arak",
          "Aşiran"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Arak",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Arak",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Aşiran",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Aşiran",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Dügah",
            "Hüseyni",
            "Neva",
            "Gerdaniye",
            "Aşiran"
          ],
          "nim_perdeler": [
            "Arak",
            "Zirgüle",
            "Eviç",
            "Hicaz",
            "Buselik",
            "Hi caz"
          ],
          "asil_perde_canonical": [
            "Dügâh",
            "Hüseynî",
            "Nevâ",
            "Gerdâniye",
            "Aşîrân"
          ]
        }
      }
    },
    {
      "id": "huseyni",
      "name_tr": "Hüseyni",
      "evidence": {
        "page_start": 52,
        "seyir_sequence": [
          "Hüseyni",
          "Muhayyer",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Neva",
          "Çargah",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Dügah",
          "Segah",
          "Çargah",
          "Hüseyni",
          "Acem",
          "Gerd miye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Dügah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Muhayyer",
            "Gerdaniye",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah"
          ],
          "nim_perdeler": [
            "Eviç",
            "Acem",
            "Gerd miye"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Muhayyer",
            "Gerdâniye",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "bestenigar",
      "name_tr": "Bestenigar",
      "evidence": {
        "page_start": 52,
        "seyir_sequence": [
          "Çargah",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah",
          "Segah",
          "Çargah",
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Saha",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Segah",
            "Dügah",
            "Gerdaniye",
            "Hüseyni",
            "Rast"
          ],
          "nim_perdeler": [
            "Saha",
            "Acem",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Gerdâniye",
            "Hüseynî",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "muhalif_arak",
      "name_tr": "Muhalif arak",
      "evidence": {
        "page_start": 52,
        "seyir_sequence": [
          "Çargah",
          "Nihavend",
          "Saha",
          "Çargah",
          "Nihavend",
          "Çargah",
          "Nihavend",
          "Dügah",
          "Nihavend",
          "Dügah",
          "Rast",
          "Dügah",
          "Arak",
          "Rast",
          "Ni havend",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Çargah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Nihavend",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Çargah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Nihavend",
            "Saha",
            "Arak",
            "Ni havend"
          ],
          "asil_perde_canonical": [
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "evic_arak",
      "name_tr": "Eviç-arak",
      "evidence": {
        "page_start": 53,
        "seyir_sequence": [
          "Eviç",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Dügah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Eviç",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Eviç",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Eviç",
            "Hicaz",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "evic",
      "name_tr": "Eviç",
      "evidence": {
        "page_start": 53,
        "seyir_sequence": [
          "Eviç",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Muhayyer",
          "Eviç",
          "Gerdaniye",
          "Hüseyni",
          "Eviç",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Çargah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Acem",
          "Hüseyni",
          "Hüseyni",
          "Acem",
          "Ger daniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Neva",
          "Beyati",
          "Acem",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Çargah",
          "Gerdaniye",
          "Acem",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Çargah",
          "Segah",
          "Segah",
          "Dügah",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Eviç",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Çargah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Eviç",
            "Acem",
            "Ger daniye",
            "Beyati"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "ruy_i_arak",
      "name_tr": "Ruy-i arak",
      "evidence": {
        "page_start": 54,
        "seyir_sequence": [
          "Eviç",
          "Tiz segah",
          "Sünbüle",
          "Gerdaniye",
          "Eviç",
          "Aceın",
          "Neva",
          "Hicaz",
          "Segah",
          "Nihavend",
          "Rast",
          "Dügah",
          "Rast",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Hüseyni",
          "Neva",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Eviç",
          "Gerdaniye",
          "Inuhayyer",
          "Eviç",
          "Ger daniye",
          "Hüseyni",
          "Eviç",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Ne va",
          "Hicaz",
          "Segah",
          "Dügah",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Dügah",
          "Segah",
          "Hicaz",
          "Neva",
          "Hi caz",
          "Segah",
          "Dügah",
          "Zirgüle",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Eviç",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Eviç",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Tiz segah",
            "Gerdaniye",
            "Neva",
            "Segah",
            "Rast",
            "Dügah",
            "Hüseyni"
          ],
          "nim_perdeler": [
            "Eviç",
            "Sünbüle",
            "Aceın",
            "Hicaz",
            "Nihavend",
            "Inuhayyer",
            "Ger daniye",
            "Ne va",
            "Zirgüle",
            "Hi caz"
          ],
          "asil_perde_canonical": [
            "Tiz Segâh",
            "Gerdâniye",
            "Nevâ",
            "Segâh",
            "Rast",
            "Dügâh",
            "Hüseynî"
          ]
        }
      }
    },
    {
      "id": "horasanek",
      "name_tr": "Horasanek",
      "evidence": {
        "page_start": 55,
        "seyir_sequence": [
          "Buselik",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Buselik",
          "Dügah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Aşiran",
          "Rast",
          "Arak",
          "Aşiran",
          "Yegah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Buselik",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Dügah",
            "Çargah",
            "Segah",
            "Rast",
            "Aşiran",
            "Yegah"
          ],
          "nim_perdeler": [
            "Buselik",
            "Hicaz",
            "Acem",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Dügâh",
            "Çargâh",
            "Segâh",
            "Rast",
            "Aşîrân",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "evic_buselik",
      "name_tr": "Eviç-buselik",
      "evidence": {
        "page_start": 55,
        "seyir_sequence": [
          "Eviç",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Eviç",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Eviç",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Muhayyer",
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Eviç",
            "Buselik",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Muhayyer",
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "n_ecd_i_horasani",
      "name_tr": "N ecd-i horasani",
      "evidence": {
        "page_start": 55,
        "seyir_sequence": [
          "Neva",
          "Muhayyer",
          "Gerdaniye",
          "Eviç",
          "Büseyni",
          "Neva",
          "Hicaz",
          "Buselik",
          "Hicaz",
          "Buselik",
          "Dügah",
          "Rast",
          "Buselik",
          "Hicaz",
          "Neva",
          "Hüsey ni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Anık"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Anık",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Muhayyer",
            "Gerdaniye",
            "Dügah",
            "Rast",
            "Çargah",
            "Segah"
          ],
          "nim_perdeler": [
            "Eviç",
            "Büseyni",
            "Hicaz",
            "Buselik",
            "Hüsey ni",
            "Anık"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Muhayyer",
            "Gerdâniye",
            "Dügâh",
            "Rast",
            "Çargâh",
            "Segâh"
          ]
        }
      }
    },
    {
      "id": "dilkes",
      "name_tr": "Dilkeş",
      "evidence": {
        "page_start": 55,
        "seyir_sequence": [
          "Hüseyni",
          "Muhayyer",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Dügah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Dügah",
          "Iıihavend",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Dügah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Muhayyer",
            "Gerdaniye",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Eviç",
            "Iıihavend",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Muhayyer",
            "Gerdâniye",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "dilkes_haveran",
      "name_tr": "Dilkeş haveran",
      "evidence": {
        "page_start": 56,
        "seyir_sequence": [
          "Arak",
          "Rast",
          "Dügillı",
          "Rast",
          "Dügillı",
          "Rast",
          "Dügillı",
          "Segah",
          "Buselik",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Aşiran",
          "Yegah",
          "Buselik",
          "Segah",
          "Dügah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Arak",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Rast",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Yegah",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Segah",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Rast",
            "Segah",
            "Dügah",
            "Aşiran",
            "Yegah"
          ],
          "nim_perdeler": [
            "Arak",
            "Dügillı",
            "Buselik"
          ],
          "asil_perde_canonical": [
            "Rast",
            "Segâh",
            "Dügâh",
            "Aşîrân",
            "Yegâh"
          ]
        }
      }
    },
    {
      "id": "muhalifekarak",
      "name_tr": "Muhalifekarak",
      "evidence": {
        "page_start": 56,
        "seyir_sequence": [
          "Segah",
          "Neva",
          "Çargah",
          "Neva",
          "Segah",
          "Çargah",
          "Segillı",
          "Nihavend",
          "Hüseyni",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Çargillı",
          "Segillı",
          "Nihavend",
          "Rast",
          "Segah",
          "Nihavend",
          "Rast",
          "Dügillı",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Segah",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Segah",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Segah",
            "Neva",
            "Çargah",
            "Hüseyni",
            "Rast"
          ],
          "nim_perdeler": [
            "Segillı",
            "Nihavend",
            "Eviç",
            "Çargillı",
            "Dügillı",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Segâh",
            "Nevâ",
            "Çargâh",
            "Hüseynî",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "gerdaniye_buselik",
      "name_tr": "Gerdaniye-buselik",
      "evidence": {
        "page_start": 56,
        "seyir_sequence": [
          "Gerdaniye",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Buselik",
          "Dügillı",
          "Rast",
          "Dügah",
          "Buselik",
          "Çargah",
          "Dügah",
          "Buselik",
          "Rast",
          "Dügah"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Gerdaniye",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Buselik",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Dügah",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Gerdaniye",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Gerdaniye",
            "Hüseyni",
            "Neva",
            "Çargah",
            "Rast",
            "Dügah"
          ],
          "nim_perdeler": [
            "Acem",
            "Buselik",
            "Dügillı"
          ],
          "asil_perde_canonical": [
            "Gerdâniye",
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Rast",
            "Dügâh"
          ]
        }
      }
    },
    {
      "id": "gerdaniye_kurdi",
      "name_tr": "Gerdaniye-kürdi",
      "evidence": {
        "page_start": 56,
        "seyir_sequence": [
          "Acem",
          "Hüseyni",
          "Acem",
          "Hüseyni",
          "Neva",
          "Be yati",
          "Neva",
          "Çargah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Neva",
          "Çargah",
          "Beyati",
          "Neva",
          "Çargah",
          "Segah",
          "Çargah",
          "Acem",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Rast",
          "Neva",
          "Çargah",
          "Kür di",
          "Dügah",
          "Rast",
          "Neva",
          "Hüseyni",
          "Neva",
          "Ger daniye",
          "EviÇ",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Çıp gah",
          "Segah",
          "Dügah",
          "Saha",
          "Çargah",
          "Segah",
          "Saha",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Segah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Acem",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Acem",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Neva",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast"
          ],
          "nim_perdeler": [
            "Acem",
            "Be yati",
            "Beyati",
            "Kür di",
            "Ger daniye",
            "EviÇ",
            "Hicaz",
            "Çıp gah",
            "Saha",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Nevâ",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast"
          ]
        }
      }
    },
    {
      "id": "rahatulervah",
      "name_tr": "Rahatülervah",
      "evidence": {
        "page_start": 57,
        "seyir_sequence": [
          "Hüseyni",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Neva",
          "Gerda niye",
          "Eviç",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Hüseyni",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Rast",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Hüseyni",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Hüseyni",
            "Neva",
            "Segah",
            "Dügah",
            "Rast",
            "Çargah"
          ],
          "nim_perdeler": [
            "Hicaz",
            "Gerda niye",
            "Eviç",
            "Arak"
          ],
          "asil_perde_canonical": [
            "Hüseynî",
            "Nevâ",
            "Segâh",
            "Dügâh",
            "Rast",
            "Çargâh"
          ]
        }
      }
    },
    {
      "id": "sultani_arak",
      "name_tr": "Sultani arak",
      "evidence": {
        "page_start": 57,
        "seyir_sequence": [
          "Neva",
          "Hüseyni",
          "Eviç",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Rast",
          "Dügah",
          "Rast",
          "Arak",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Rast",
          "Neva",
          "Hüseyni",
          "Neva",
          "Gerdaniye",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Gerdaniye",
          "Hüseyni",
          "Eviç",
          "Muhayyer",
          "Şehnaz",
          "Eviç",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Neva",
          "Hüseyni",
          "Neva",
          "Hicaz",
          "Segah",
          "Dügah",
          "Rast",
          "Arak",
          "Rast",
          "Arak",
          "Aşiran",
          "Segah",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Neva",
          "Hüseyni",
          "Neva",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Dügah",
          "Segah",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Çargah",
          "Segah",
          "Dügah",
          "Rast",
          "Arak"
        ]
      },
      "analysis": {
        "agaz": {
          "perde": "Neva",
          "source": "explicit_in_sequence_start"
        },
        "merkez": {
          "perde": "Neva",
          "source": "derived_from_sequence_frequency"
        },
        "karar": {
          "perde": "Arak",
          "source": "explicit_in_sequence_end"
        },
        "alt_sinir": {
          "perde": "Aşiran",
          "source": "derived_from_rank_order"
        },
        "ust_sinir": {
          "perde": "Muhayyer",
          "source": "derived_from_rank_order"
        },
        "kullanilan_perdeler": {
          "asil_perdeler": [
            "Neva",
            "Hüseyni",
            "Gerdaniye",
            "Çargah",
            "Segah",
            "Dügah",
            "Rast",
            "Muhayyer",
            "Aşiran"
          ],
          "nim_perdeler": [
            "Eviç",
            "Arak",
            "Şehnaz",
            "Hicaz"
          ],
          "asil_perde_canonical": [
            "Nevâ",
            "Hüseynî",
            "Gerdâniye",
            "Çargâh",
            "Segâh",
            "Dügâh",
            "Rast",
            "Muhayyer",
            "Aşîrân"
          ]
        }
      }
    }
  ],
  "classification": {
    "rule": "Perde adı normalize edilip ASIL_MAP anahtarlarıyla eşleşirse 'asil', aksi halde 'nim'.",
    "asil_map": {
      "yegah": "Yegâh",
      "asiran": "Aşîrân",
      "irak": "Irâk",
      "rast": "Rast",
      "dugah": "Dügâh",
      "segah": "Segâh",
      "cargah": "Çargâh",
      "neva": "Nevâ",
      "huseyni": "Hüseynî",
      "evc": "Evc",
      "gerdaniye": "Gerdâniye",
      "muhayyer": "Muhayyer",
      "tiz segah": "Tiz Segâh",
      "tiz cargah": "Tiz Çargâh",
      "tiz neva": "Tiz Nevâ"
    },
    "normalization": "lowercase + dotless-i normalize + NFKD + combining strip + tr->ascii + punctuation strip + whitespace collapse"
  }
}
