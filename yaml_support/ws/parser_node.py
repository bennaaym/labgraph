import asyncio
import os
from labgraph import (
    AsyncPublisher,
    Config,
    Group,
    Node,
    Topic,
    Connections,
    publisher,
)
from labgraph.websockets.ws_server.ws_api_node_server import (
    WSAPIServerConfig,
    WSAPIServerNode
)
from labgraph.websockets.ws_server.ws_server_stream_message import WSStreamMessage
from yaml_support.ws.enums import ENUMS
from yaml_support.yamlify import yamlify
from yaml_support.edge_list_generator import edge_list_generator

import ntpath


# Constants
SAMPLE_RATE = 60


class ParserNodeConfig(Config):
    should_terminate: bool = False
    path:str

class ParserNode(Node):
    """
    Node for parsing the current running labgraph file 
    and sending messages to a `WSAPIServerNode`.
    """

    TOPIC = Topic(WSStreamMessage)
    config: ParserNodeConfig

    @publisher(TOPIC)
    async def source(self) -> AsyncPublisher:
        edge_list = edge_list_generator(yamlify(self.config.path))
        await asyncio.sleep(.01)
        while True:
            sample = edge_list
            msg = WSStreamMessage(
                samples=sample,
                stream_name=ENUMS.STREAM.LABGRAPH_MONITOR,
                stream_id=ENUMS.STREAM.LABGRAPH_MONITOR_ID,
            )
            yield self.TOPIC, msg
            await asyncio.sleep(1 / SAMPLE_RATE)

        # if self.config.should_terminate:
        #     Give the graph time to propagate the messages
        #     await asyncio.sleep(0.1)
        #     raise NormalTermination()


class WSSenderConfig(Config):
    path:str


class WSSenderNode(Group):
    PARSER_NODE: ParserNode
    WS_SERVER_NODE: WSAPIServerNode
    config: WSSenderConfig

    def setup(self) -> None:
        wsapi_server_config = WSAPIServerConfig(
            app_id="test_app",
            ip=ENUMS.WS_SERVER.DEFAULT_IP,
            port=ENUMS.WS_SERVER.DEFAULT_PORT,
            api_version=ENUMS.WS_SERVER.DEFAULT_API_VERSION,
            num_messages=-1,
            enums=ENUMS(),
            sample_rate=SAMPLE_RATE,
        )
        self.PARSER_NODE.configure(ParserNodeConfig(path = self.config.path))
        self.WS_SERVER_NODE.configure(wsapi_server_config)

    def connections(self) -> Connections:
        return ((self.PARSER_NODE.TOPIC, self.WS_SERVER_NODE.topic),)