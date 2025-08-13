import os
import time
import json
import ipaddress
import requests
import pyshark

API_KEY = os.getenv("SECRET_API_KEY")

def is_public(ip: str) -> bool:
    try:
        return ipaddress.ip_address(ip).is_global
    except ValueError:
        return False

def read_pcap(pcap_path):
    """Return ordered, deduped list of public source IPv4s from the pcap."""
    src_ips = []
    cap = pyshark.FileCapture(pcap_path, display_filter='ip', keep_packets=False)
    for pkt in cap:
        try:
            src_ips.append(pkt.ip.src)
        except AttributeError:
            continue
    cap.close()
    # dedupe but keep first-seen order, filter to public
    return [ip for ip in dict.fromkeys(src_ips) if is_public(ip)]

def geolocate_single(ips, api_key, sleep=0.4):
    if not api_key:
        raise RuntimeError("SECRET_API_KEY not set.")
    url = "https://api.ipgeolocation.io/ipgeo"
    results = []
    with requests.Session() as s:
        for ip in ips:
            r = s.get(url, params={"apiKey": api_key, "ip": ip}, timeout=15)
            r.raise_for_status()
            results.append(r.json())
            time.sleep(sleep)  # be nice to the API / avoid rate limits
    return results

def main():
    ips = read_pcap(r"D:\Downloads\friends.pcapng")
    print(f"[+] Unique public source IPs: {len(ips)}")
    geo = geolocate_single(ips, API_KEY)

    with open("ip_geolocation.json", "w") as f:
        json.dump(geo, f, indent=2)

    print("[+] Wrote ip_geolocation.json")

if __name__ == "__main__":
    main()
