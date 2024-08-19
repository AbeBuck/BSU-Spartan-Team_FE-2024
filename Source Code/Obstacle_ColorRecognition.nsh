{
    "functionList": {
        "function_1": {
            "param_0": {
                "paramname": "Color Recognition Threshold: ",
                "type": 3
            },
            "param_1": {
                "paramname": "greenThreshold",
                "type": 2
            },
            "param_2": {
                "paramname": "green",
                "type": 3
            },
            "param_3": {
                "paramname": "redThreshold",
                "type": 2
            },
            "param_4": {
                "paramname": "red",
                "type": 3
            }
        }
    },
    "notes": {
    },
    "top_0": {
        "item_0000000000": {
            "disabled": "0",
            "opcode": "",
            "x": "5735",
            "y": "87"
        }
    },
    "top_1": {
        "item_0000000008": {
            "disabled": "0",
            "opcode": "operator_and",
            "param_0": {
                "item_0000000006": {
                    "disabled": "0",
                    "opcode": "operator_logic",
                    "param_0": {
                        "item_0000000002": {
                            "disabled": "0",
                            "opcode": "operator_math",
                            "param_0": {
                                "item_0000000001": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "x": "6361",
                                    "y": "167"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_2": {
                                "opcode": "CGraphicsTextItem",
                                "position": "2",
                                "type": "10",
                                "value": "10"
                            },
                            "x": "6346",
                            "y": "162"
                        },
                        "opcode": "operator_math",
                        "position": "0",
                        "type": "10"
                    },
                    "param_1": {
                        "position": "1",
                        "type": "11",
                        "value": "1"
                    },
                    "param_2": {
                        "item_0000000005": {
                            "disabled": "0",
                            "opcode": "operator_math",
                            "param_0": {
                                "item_0000000003": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "6999",
                                    "y": "167"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "4"
                            },
                            "param_2": {
                                "item_0000000004": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "x": "7546",
                                    "y": "167"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "2",
                                "type": "10"
                            },
                            "x": "6984",
                            "y": "162"
                        },
                        "opcode": "operator_math",
                        "position": "2",
                        "type": "10"
                    },
                    "x": "6326",
                    "y": "157"
                },
                "opcode": "operator_logic",
                "position": "0",
                "type": "12"
            },
            "param_2": {
                "item_0000000007": {
                    "disabled": "0",
                    "opcode": "empty",
                    "x": "8059",
                    "y": "172"
                },
                "opcode": "empty",
                "position": "2",
                "type": "12"
            },
            "x": "6316",
            "y": "152"
        }
    },
    "top_2": {
        "item_0000000016": {
            "disabled": "0",
            "opcode": "operator_and",
            "param_0": {
                "item_0000000014": {
                    "disabled": "0",
                    "opcode": "operator_logic",
                    "param_0": {
                        "item_0000000010": {
                            "disabled": "0",
                            "opcode": "operator_math",
                            "param_0": {
                                "item_0000000009": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "x": "6342",
                                    "y": "362"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_2": {
                                "opcode": "CGraphicsTextItem",
                                "position": "2",
                                "type": "10",
                                "value": "10"
                            },
                            "x": "6327",
                            "y": "357"
                        },
                        "opcode": "operator_math",
                        "position": "0",
                        "type": "10"
                    },
                    "param_1": {
                        "position": "1",
                        "type": "11",
                        "value": "1"
                    },
                    "param_2": {
                        "item_0000000013": {
                            "disabled": "0",
                            "opcode": "operator_math",
                            "param_0": {
                                "item_0000000011": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "6982",
                                    "y": "362"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "4"
                            },
                            "param_2": {
                                "item_0000000012": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "x": "7531",
                                    "y": "362"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "2",
                                "type": "10"
                            },
                            "x": "6967",
                            "y": "357"
                        },
                        "opcode": "operator_math",
                        "position": "2",
                        "type": "10"
                    },
                    "x": "6307",
                    "y": "352"
                },
                "opcode": "operator_logic",
                "position": "0",
                "type": "12"
            },
            "param_2": {
                "item_0000000015": {
                    "disabled": "0",
                    "opcode": "empty",
                    "x": "8046",
                    "y": "367"
                },
                "opcode": "empty",
                "position": "2",
                "type": "12"
            },
            "x": "6297",
            "y": "347"
        }
    },
    "top_3": {
        "item_0000000017": {
            "disabled": "0",
            "noteItem": {
                "text": "past",
                "x": "6680.33",
                "y": "676.556"
            },
            "opcode": "camera_recoColorRGB_more",
            "param_0": {
                "position": "0",
                "type": "11",
                "value": "1"
            },
            "param_11": {
                "opcode": "CGraphicsTextItem",
                "position": "11",
                "type": "10",
                "value": "-21"
            },
            "param_13": {
                "opcode": "CGraphicsTextItem",
                "position": "13",
                "type": "10",
                "value": "9"
            },
            "param_15": {
                "opcode": "CGraphicsTextItem",
                "position": "15",
                "type": "10",
                "value": "38"
            },
            "param_17": {
                "opcode": "CGraphicsTextItem",
                "position": "17",
                "type": "10",
                "value": "0"
            },
            "param_19": {
                "opcode": "CGraphicsTextItem",
                "position": "19",
                "type": "10",
                "value": "0"
            },
            "param_2": {
                "position": "2",
                "type": "11",
                "value": "1"
            },
            "param_21": {
                "opcode": "CGraphicsTextItem",
                "position": "21",
                "type": "10",
                "value": "160"
            },
            "param_23": {
                "opcode": "CGraphicsTextItem",
                "position": "23",
                "type": "10",
                "value": "120"
            },
            "param_3": {
                "position": "3",
                "type": "11",
                "value": "1"
            },
            "param_5": {
                "opcode": "CGraphicsTextItem",
                "position": "5",
                "type": "10",
                "value": "0"
            },
            "param_7": {
                "opcode": "CGraphicsTextItem",
                "position": "7",
                "type": "10",
                "value": "100"
            },
            "param_9": {
                "opcode": "CGraphicsTextItem",
                "position": "9",
                "type": "10",
                "value": "-75"
            },
            "x": "6111",
            "y": "677"
        },
        "item_0000000018": {
            "disabled": "0",
            "opcode": "camera_recoColorRGB_more",
            "param_0": {
                "position": "0",
                "type": "11",
                "value": "1"
            },
            "param_11": {
                "opcode": "CGraphicsTextItem",
                "position": "11",
                "type": "10",
                "value": "127"
            },
            "param_13": {
                "opcode": "CGraphicsTextItem",
                "position": "13",
                "type": "10",
                "value": "-128"
            },
            "param_15": {
                "opcode": "CGraphicsTextItem",
                "position": "15",
                "type": "10",
                "value": "127"
            },
            "param_17": {
                "opcode": "CGraphicsTextItem",
                "position": "17",
                "type": "10",
                "value": "0"
            },
            "param_19": {
                "opcode": "CGraphicsTextItem",
                "position": "19",
                "type": "10",
                "value": "0"
            },
            "param_2": {
                "position": "2",
                "type": "11",
                "value": "1"
            },
            "param_21": {
                "opcode": "CGraphicsTextItem",
                "position": "21",
                "type": "10",
                "value": "160"
            },
            "param_23": {
                "opcode": "CGraphicsTextItem",
                "position": "23",
                "type": "10",
                "value": "120"
            },
            "param_3": {
                "position": "3",
                "type": "11",
                "value": "2"
            },
            "param_5": {
                "opcode": "CGraphicsTextItem",
                "position": "5",
                "type": "10",
                "value": "100"
            },
            "param_7": {
                "opcode": "CGraphicsTextItem",
                "position": "7",
                "type": "10",
                "value": "0"
            },
            "param_9": {
                "opcode": "CGraphicsTextItem",
                "position": "9",
                "type": "10",
                "value": "22"
            },
            "x": "6111",
            "y": "897"
        }
    },
    "top_4": {
        "item_0000000019": {
            "blocktype": 6,
            "disabled": "0",
            "function_1": {
                "param_0": {
                    "paramname": "Color Recognition Threshold: ",
                    "type": 3
                },
                "param_1": {
                    "paramname": "greenThreshold",
                    "type": 2
                },
                "param_2": {
                    "paramname": "green",
                    "type": 3
                },
                "param_3": {
                    "paramname": "redThreshold",
                    "type": 2
                },
                "param_4": {
                    "paramname": "red",
                    "type": 3
                }
            },
            "opcode": "function_1",
            "param_0": {
                "opcode": "CGraphicsTextItem",
                "position": "0",
                "type": "9",
                "value": "Color Recognition Threshold: "
            },
            "param_1": {
                "position": "1",
                "type": "9"
            },
            "param_2": {
                "opcode": "CGraphicsTextItem",
                "position": "2",
                "type": "9",
                "value": "green"
            },
            "param_3": {
                "position": "3",
                "type": "9"
            },
            "param_4": {
                "opcode": "CGraphicsTextItem",
                "position": "4",
                "type": "9",
                "value": "red"
            },
            "x": "5697",
            "y": "10"
        },
        "item_0000000036": {
            "disabled": "0",
            "opcode": "control_ifelse",
            "param_1": {
                "item_0000000026": {
                    "disabled": "0",
                    "opcode": "operator_and",
                    "param_0": {
                        "item_0000000022": {
                            "disabled": "0",
                            "opcode": "operator_logic",
                            "param_0": {
                                "item_0000000020": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "5758",
                                    "y": "85"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_2": {
                                "item_0000000021": {
                                    "ParamIndex": 0,
                                    "opcode": "",
                                    "pDependOn": "function_1",
                                    "paramName": "greenThreshold",
                                    "paramType": 2,
                                    "x": "6308",
                                    "y": "85"
                                },
                                "opcode": "",
                                "position": "2",
                                "type": "10"
                            },
                            "x": "5738",
                            "y": "80"
                        },
                        "opcode": "operator_logic",
                        "position": "0",
                        "type": "12"
                    },
                    "param_2": {
                        "item_0000000025": {
                            "disabled": "0",
                            "opcode": "operator_logic",
                            "param_0": {
                                "item_0000000023": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "6555",
                                    "y": "85"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_2": {
                                "item_0000000024": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "7105",
                                    "y": "85"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "2",
                                "type": "10"
                            },
                            "x": "6535",
                            "y": "80"
                        },
                        "opcode": "operator_logic",
                        "position": "2",
                        "type": "12"
                    },
                    "x": "5728",
                    "y": "75"
                },
                "opcode": "operator_and",
                "position": "1",
                "type": "12"
            },
            "substack1": {
                "item_0000000027": {
                    "disabled": "0",
                    "opcode": "MakerLED_ALLColorLED",
                    "param_1": {
                        "position": "1",
                        "type": "11",
                        "value": "1"
                    },
                    "param_3": {
                        "position": "3",
                        "type": "13",
                        "value": "#0000ff"
                    },
                    "x": "5717",
                    "y": "140"
                },
                "item_0000000028": {
                    "disabled": "0",
                    "opcode": "MakerLED_ALLColorLED",
                    "param_1": {
                        "position": "1",
                        "type": "11",
                        "value": "3"
                    },
                    "param_3": {
                        "position": "3",
                        "type": "13",
                        "value": "#0000ff"
                    },
                    "x": "5717",
                    "y": "190"
                },
                "type": "15"
            },
            "substack2": {
                "item_0000000035": {
                    "disabled": "0",
                    "opcode": "control_ifelse",
                    "param_1": {
                        "item_0000000031": {
                            "disabled": "0",
                            "opcode": "operator_logic",
                            "param_0": {
                                "item_0000000029": {
                                    "disabled": "0",
                                    "opcode": "get_recoColorRGB_more",
                                    "param_0": {
                                        "position": "0",
                                        "type": "11",
                                        "value": "1"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "2"
                                    },
                                    "param_3": {
                                        "position": "3",
                                        "type": "11",
                                        "value": "3"
                                    },
                                    "x": "5768",
                                    "y": "280"
                                },
                                "opcode": "get_recoColorRGB_more",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_2": {
                                "item_0000000030": {
                                    "ParamIndex": 1,
                                    "opcode": "",
                                    "pDependOn": "function_1",
                                    "paramName": "redThreshold",
                                    "paramType": 2,
                                    "x": "6320",
                                    "y": "280"
                                },
                                "opcode": "",
                                "position": "2",
                                "type": "10"
                            },
                            "x": "5748",
                            "y": "275"
                        },
                        "opcode": "operator_logic",
                        "position": "1",
                        "type": "12"
                    },
                    "substack1": {
                        "item_0000000032": {
                            "disabled": "0",
                            "opcode": "MakerLED_ALLColorLED",
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_3": {
                                "position": "3",
                                "type": "13",
                                "value": "#ff0000"
                            },
                            "x": "5737",
                            "y": "330"
                        },
                        "item_0000000033": {
                            "disabled": "0",
                            "opcode": "MakerLED_ALLColorLED",
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "3"
                            },
                            "param_3": {
                                "position": "3",
                                "type": "13",
                                "value": "#ff0000"
                            },
                            "x": "5737",
                            "y": "380"
                        },
                        "type": "15"
                    },
                    "substack2": {
                        "item_0000000034": {
                            "disabled": "0",
                            "opcode": "MakerLED_CloseColorLED",
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "6"
                            },
                            "x": "5737",
                            "y": "460"
                        },
                        "type": "16"
                    },
                    "x": "5717",
                    "y": "270"
                },
                "type": "16"
            },
            "x": "5697",
            "y": "70"
        }
    },
    "top_5": {
        "item_0000000037": {
            "disabled": "0",
            "opcode": "main",
            "x": "5000",
            "y": "0"
        },
        "item_0000000038": {
            "disabled": "0",
            "opcode": "camera_recoColorRGB_more",
            "param_0": {
                "position": "0",
                "type": "11",
                "value": "1"
            },
            "param_11": {
                "opcode": "CGraphicsTextItem",
                "position": "11",
                "type": "10",
                "value": "-15"
            },
            "param_13": {
                "opcode": "CGraphicsTextItem",
                "position": "13",
                "type": "10",
                "value": "9"
            },
            "param_15": {
                "opcode": "CGraphicsTextItem",
                "position": "15",
                "type": "10",
                "value": "50"
            },
            "param_17": {
                "opcode": "CGraphicsTextItem",
                "position": "17",
                "type": "10",
                "value": "0"
            },
            "param_19": {
                "opcode": "CGraphicsTextItem",
                "position": "19",
                "type": "10",
                "value": "0"
            },
            "param_2": {
                "position": "2",
                "type": "11",
                "value": "1"
            },
            "param_21": {
                "opcode": "CGraphicsTextItem",
                "position": "21",
                "type": "10",
                "value": "160"
            },
            "param_23": {
                "opcode": "CGraphicsTextItem",
                "position": "23",
                "type": "10",
                "value": "120"
            },
            "param_3": {
                "position": "3",
                "type": "11",
                "value": "1"
            },
            "param_5": {
                "opcode": "CGraphicsTextItem",
                "position": "5",
                "type": "10",
                "value": "0"
            },
            "param_7": {
                "opcode": "CGraphicsTextItem",
                "position": "7",
                "type": "10",
                "value": "100"
            },
            "param_9": {
                "opcode": "CGraphicsTextItem",
                "position": "9",
                "type": "10",
                "value": "-128"
            },
            "x": "5000",
            "y": "55"
        },
        "item_0000000039": {
            "disabled": "0",
            "opcode": "camera_recoColorRGB_more",
            "param_0": {
                "position": "0",
                "type": "11",
                "value": "1"
            },
            "param_11": {
                "opcode": "CGraphicsTextItem",
                "position": "11",
                "type": "10",
                "value": "127"
            },
            "param_13": {
                "opcode": "CGraphicsTextItem",
                "position": "13",
                "type": "10",
                "value": "-50"
            },
            "param_15": {
                "opcode": "CGraphicsTextItem",
                "position": "15",
                "type": "10",
                "value": "127"
            },
            "param_17": {
                "opcode": "CGraphicsTextItem",
                "position": "17",
                "type": "10",
                "value": "0"
            },
            "param_19": {
                "opcode": "CGraphicsTextItem",
                "position": "19",
                "type": "10",
                "value": "0"
            },
            "param_2": {
                "position": "2",
                "type": "11",
                "value": "1"
            },
            "param_21": {
                "opcode": "CGraphicsTextItem",
                "position": "21",
                "type": "10",
                "value": "160"
            },
            "param_23": {
                "opcode": "CGraphicsTextItem",
                "position": "23",
                "type": "10",
                "value": "120"
            },
            "param_3": {
                "position": "3",
                "type": "11",
                "value": "2"
            },
            "param_5": {
                "opcode": "CGraphicsTextItem",
                "position": "5",
                "type": "10",
                "value": "0"
            },
            "param_7": {
                "opcode": "CGraphicsTextItem",
                "position": "7",
                "type": "10",
                "value": "100"
            },
            "param_9": {
                "opcode": "CGraphicsTextItem",
                "position": "9",
                "type": "10",
                "value": "22"
            },
            "x": "5000",
            "y": "275"
        },
        "item_0000000040": {
            "disabled": "0",
            "opcode": "data_setvariableto",
            "param_1": {
                "position": "1",
                "type": "11",
                "value": "1"
            },
            "param_3": {
                "opcode": "CGraphicsTextItem",
                "position": "3",
                "type": "10",
                "value": "0"
            },
            "x": "5000",
            "y": "495"
        },
        "item_0000000054": {
            "disabled": "0",
            "opcode": "control_forever",
            "substack1": {
                "item_0000000047": {
                    "disabled": "0",
                    "opcode": "control_if",
                    "param_1": {
                        "item_0000000043": {
                            "disabled": "0",
                            "opcode": "operator_logic",
                            "param_0": {
                                "item_0000000042": {
                                    "disabled": "0",
                                    "opcode": "operator_math",
                                    "param_0": {
                                        "item_0000000041": {
                                            "blocktype": 5,
                                            "opcode": "variable_i",
                                            "varname": "i",
                                            "x": "5086",
                                            "y": "610"
                                        },
                                        "opcode": "variable_i",
                                        "position": "0",
                                        "type": "10"
                                    },
                                    "param_1": {
                                        "position": "1",
                                        "type": "11",
                                        "value": "5"
                                    },
                                    "param_2": {
                                        "opcode": "CGraphicsTextItem",
                                        "position": "2",
                                        "type": "10",
                                        "value": "720"
                                    },
                                    "x": "5071",
                                    "y": "605"
                                },
                                "opcode": "operator_math",
                                "position": "0",
                                "type": "10"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "3"
                            },
                            "param_2": {
                                "opcode": "CGraphicsTextItem",
                                "position": "2",
                                "type": "10",
                                "value": "0"
                            },
                            "x": "5051",
                            "y": "600"
                        },
                        "opcode": "operator_logic",
                        "position": "1",
                        "type": "12"
                    },
                    "substack1": {
                        "item_0000000044": {
                            "disabled": "0",
                            "opcode": "Maker_displayFont",
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "x": "5040",
                            "y": "665"
                        },
                        "item_0000000045": {
                            "disabled": "0",
                            "opcode": "Maker_displayWordsPos",
                            "param_1": {
                                "opcode": "CGraphicsTextItem",
                                "position": "1",
                                "type": "10",
                                "value": "gPix"
                            },
                            "param_3": {
                                "opcode": "CGraphicsTextItem",
                                "position": "3",
                                "type": "10",
                                "value": "5"
                            },
                            "param_5": {
                                "opcode": "CGraphicsTextItem",
                                "position": "5",
                                "type": "10",
                                "value": "0"
                            },
                            "x": "5040",
                            "y": "715"
                        },
                        "item_0000000046": {
                            "disabled": "0",
                            "opcode": "Maker_displayWordsPos",
                            "param_1": {
                                "opcode": "CGraphicsTextItem",
                                "position": "1",
                                "type": "10",
                                "value": "rPix"
                            },
                            "param_3": {
                                "opcode": "CGraphicsTextItem",
                                "position": "3",
                                "type": "10",
                                "value": "5"
                            },
                            "param_5": {
                                "opcode": "CGraphicsTextItem",
                                "position": "5",
                                "type": "10",
                                "value": "16"
                            },
                            "x": "5040",
                            "y": "765"
                        },
                        "type": "15"
                    },
                    "x": "5020",
                    "y": "595"
                },
                "item_0000000049": {
                    "disabled": "0",
                    "opcode": "Maker_displayWordsPos",
                    "param_1": {
                        "item_0000000048": {
                            "disabled": "0",
                            "opcode": "get_recoColorRGB_more",
                            "param_0": {
                                "position": "0",
                                "type": "11",
                                "value": "1"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "1"
                            },
                            "param_3": {
                                "position": "3",
                                "type": "11",
                                "value": "3"
                            },
                            "x": "5148",
                            "y": "850"
                        },
                        "opcode": "get_recoColorRGB_more",
                        "position": "1",
                        "type": "10"
                    },
                    "param_3": {
                        "opcode": "CGraphicsTextItem",
                        "position": "3",
                        "type": "10",
                        "value": "50"
                    },
                    "param_5": {
                        "opcode": "CGraphicsTextItem",
                        "position": "5",
                        "type": "10",
                        "value": "0"
                    },
                    "x": "5020",
                    "y": "845"
                },
                "item_0000000051": {
                    "disabled": "0",
                    "opcode": "Maker_displayWordsPos",
                    "param_1": {
                        "item_0000000050": {
                            "disabled": "0",
                            "opcode": "get_recoColorRGB_more",
                            "param_0": {
                                "position": "0",
                                "type": "11",
                                "value": "1"
                            },
                            "param_1": {
                                "position": "1",
                                "type": "11",
                                "value": "2"
                            },
                            "param_3": {
                                "position": "3",
                                "type": "11",
                                "value": "3"
                            },
                            "x": "5148",
                            "y": "900"
                        },
                        "opcode": "get_recoColorRGB_more",
                        "position": "1",
                        "type": "10"
                    },
                    "param_3": {
                        "opcode": "CGraphicsTextItem",
                        "position": "3",
                        "type": "10",
                        "value": "50"
                    },
                    "param_5": {
                        "opcode": "CGraphicsTextItem",
                        "position": "5",
                        "type": "10",
                        "value": "16"
                    },
                    "x": "5020",
                    "y": "895"
                },
                "item_0000000052": {
                    "disabled": "0",
                    "opcode": "function_1",
                    "param_1": {
                        "opcode": "CGraphicsTextItem",
                        "position": "1",
                        "type": "10",
                        "value": "150"
                    },
                    "param_3": {
                        "opcode": "CGraphicsTextItem",
                        "position": "3",
                        "type": "10",
                        "value": "180"
                    },
                    "x": "5020",
                    "y": "945"
                },
                "item_0000000053": {
                    "disabled": "0",
                    "opcode": "data_changevariableby",
                    "param_1": {
                        "position": "1",
                        "type": "11",
                        "value": "1"
                    },
                    "param_3": {
                        "opcode": "CGraphicsTextItem",
                        "position": "3",
                        "type": "10",
                        "value": "1"
                    },
                    "x": "5020",
                    "y": "995"
                },
                "type": "15"
            },
            "x": "5000",
            "y": "545"
        }
    },
    "varList": [
        "i"
    ]
}
