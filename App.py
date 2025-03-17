import json

# Option 1: Load JSON from a file (uncomment if using a file)
# with open('traffic_data.json', 'r') as file:
#     traffic_data = json.load(file)

# Option 2: Paste the JSON directly here (replace with your actual JSON)


with open('traffic.json', 'r') as file:
    traffic_data = json.load(file)


def aggregate_traffic(data):
    # Initialize counters for sent and received traffic (in kilobytes)
    total_sent_kb = 0
    total_recv_kb = 0

    # Sum sent and received traffic
    for entry in data:
        total_sent_kb += entry.get("sent", 0)  # Default to 0 if field is missing
        total_recv_kb += entry.get("recv", 0)  # Default to 0 if field is missing

    # Convert from kilobytes to bytes
    total_sent_bytes = total_sent_kb * 1024
    total_recv_bytes = total_recv_kb * 1024
    total_traffic_bytes = total_sent_bytes + total_recv_bytes

    # Convert to GB and TB for display
    total_sent_gb = total_sent_bytes / (1024 ** 3)  # Bytes to GB
    total_recv_gb = total_recv_bytes / (1024 ** 3)  # Bytes to GB
    total_traffic_gb = total_traffic_bytes / (1024 ** 3)  # Bytes to GB
    total_traffic_tb = total_traffic_bytes / (1024 ** 4)  # Bytes to TB

    return {
        "sent_gb": total_sent_gb,
        "recv_gb": total_recv_gb,
        "total_traffic_gb": total_traffic_gb,
        "total_traffic_tb": total_traffic_tb
    }


def display_traffic(traffic_summary):
    print("Traffic Summary:")
    print(f"Total Sent: {traffic_summary['sent_gb']:.2f} GB")
    print(f"Total Received: {traffic_summary['recv_gb']:.2f} GB")
    print(f"Total Traffic: {traffic_summary['total_traffic_gb']:.2f} GB")
    print(f"Total Traffic: {traffic_summary['total_traffic_tb']:.2f} TB")


def main():
    # Aggregate the traffic data
    traffic_summary = aggregate_traffic(traffic_data)

    # Display the results
    display_traffic(traffic_summary)


if __name__ == "__main__":
    main()