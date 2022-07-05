from app import create_app
from flask import render_template
import time
app = create_app()

TITLE_INTERZONE = 'signaling internet_unsafe'

list_zone_origin = [
    {
        "name": "Eth-Trunk17.10",
        "flag": True
    }
]
list_zone_destiny = [
    {
        "name": "Eth-Trunk18.252",
        "flag": True
    },
    {
        "name": "Eth-Trunk18.112",
        "flag": False
    }
]
list_interzone_access = [
    {
        "name": "packet-filter 3270 inbound",
        "data": [
            {
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two":{
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING":"NO"
            },
{
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            },
{
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            },
{
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            },
{
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            },
{
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            }
        ]
    },
    {
        "name": "packet-filter 3275 outbound",
        "data": [
            {
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            }
        ]
    },
    {
        "name": "nat outbound 3375 address-group 12",
        "data": [
            {
                "table_one": {
                    "device": "MXTLAM01RTCOREDATA01",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "STATIC",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREISP07",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.64/30",
                        "INTERFACE_DESTINO": ["Eth-Trunk17.10", "Eth-Trunk17.17"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "MXTLAM01RTCOREDATA01",
                    },
                    "HIT": "0 times matched",
                    "NAT": "NO",
                    "NAT_POOL": "NO",
                    "ROUTING_OK_INTERZONA": "SI"
                },
                "table_two": {
                    "device": "MXTLAM01RTCOREDATA02",
                    "ACL": "rule 5 permit sctp source 213.131.129.76 0 destination 201.175.131.66 0",
                    "VRF": "Nextel_Signaling",
                    "origin": {
                        "ROUTING_ORIGEN": "No hay routing",
                        "INTERFACE_ORIGEN": [],
                        "TIPO_DE_ROUTING": "",
                        "NETWORK_ELEMENT_ROUTING": "",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.68/30",
                        "INTERFACE_DESTINO": ["Tunnel0/0/12"],
                        "TIPO_DE_ROUTING": "IBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-MXTLAM01RTCOREMOB07-primary",
                    },
                    "ROUTING_OK": "NO"
                },
                "table_three": {
                    "device": "MXTLAM01RTCOREDATA03",
                    "ACL": "rule 45 permit sctp source 10.10.50.0 0.0.0.7 destination 201.175.131.66 0",
                    "origin": {
                        "ROUTING_ORIGEN": "0.0.0.0/0",
                        "INTERFACE_ORIGEN": ["Eth-Trunk7.4"],
                        "TIPO_DE_ROUTING": "EBGP",
                        "NETWORK_ELEMENT_ROUTING": "To-TRANSTELCO-ISP-ATT-NBUQTD",
                    },
                    "destiny": {
                        "ROUTING_DESTINO": "201.175.131.0/24",
                        "INTERFACE_DESTINO": ["Eth-Trunk18.112"],
                        "TIPO_DE_ROUTING": "OSPF",
                        "NETWORK_ELEMENT_ROUTING": "	MX-MEX-M1-ISP-E8160E-1",
                    },
                    "ROUTING_OK": "NO"
                },
                "OPERATIIVA_A_NIVEL_ROUTING": "NO"
            }
        ]
    },
]


@app.route("/")
def index():
    return render_template('security_output.html',
                           title=TITLE_INTERZONE,
                           time=time.strftime('%A %B, %d %Y %H:%M:%S'),
                           list_zone_origin=list_zone_origin,
                           list_zone_destiny=list_zone_destiny,
                           list_interzone_access=list_interzone_access)
