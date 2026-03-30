#!/usr/bin/env python

import sys
import argparse
import rclpy

from ros_tcp_endpoint import TcpServer


def main(args=None):
    if args is None:
        args = sys.argv

    if "--ros-args" in args:
        i = args.index("--ros-args")
        app_args = args[1:i]
        ros_args = [args[0]] + args[i:]
    else:
        app_args = args[1:]
        ros_args = [args[0]]

    parser = argparse.ArgumentParser()
    parser.add_argument("yaml_path")
    parsed = parser.parse_args(app_args)

    rclpy.init(args=ros_args)
    tcp_server = TcpServer("UnityEndpoint", parsed.yaml_path)

    tcp_server.start()

    tcp_server.setup_executor()

    tcp_server.destroy_nodes()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
