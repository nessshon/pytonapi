from pytonapi.async_tonapi.client import AsyncTonapiClient
from pytonapi.schema.traces import Trace


class TraceMethod(AsyncTonapiClient):

    async def get_trace(self, trace_id: str) -> Trace:
        """
        Get the trace by trace ID or hash of any transaction in trace.

        :param trace_id: trace ID or transaction hash in hex (without 0x) or base64url format
        :return: :class:`Trace`
        """
        method = f"v2/traces/{trace_id}"
        response = await self._get(method=method)

        return Trace(**response)
