-module(module).
-compile(export_all).

-behaviour(gen_server).
-export([init/1, handle_call/3, handle_cast/2, handle_info/2, terminate/2, code_change/3]).
-define(TCP_OPTIONS,[list, {packet, 0}, {active, false}, {reuseaddr, true}]).
% server port
-define(TCP_LISTEN_PORT, 4444).

start() ->
  gen_server:start_link({local, ?MODULE}, ?MODULE, [], []).

stop(Module) ->
  gen_server:call(Module, stop).

stop() ->
  stop(?MODULE).

state(Module) ->
  gen_server:call(Module, state).

state() ->
  state(?MODULE).

% init server, open port
init([]) ->
  Pid = listen(?TCP_LISTEN_PORT),
  spawn_link(os, cmd, ["python ../ui/pui.py"]),
  {ok, [Pid]}.


handle_call(stop, _From, State) ->
  [Parent_PID | NewState] = State,
  %close listening thread
  exit(Parent_PID, "exit"),
  {stop, normal, stopped, NewState};

handle_call(state, _From, State) ->
  {reply, State, State};

handle_call(_Request, _From, State) ->
  {reply, ok, State}.


handle_cast(_Msg, State) ->
  {noreply, State}.


handle_info(_Info, State) ->
  {noreply, State}.


terminate(_Reason, _State) ->
  ok.


code_change(_OldVsn, State, _Extra) ->
  {ok, State}.


% create server port, spawn listener
listen(Port) ->
    {ok, LSocket} = gen_tcp:listen(Port, ?TCP_OPTIONS),
	spawn_link(module, do_accept, [LSocket]).

% cautch inbound data, spawn response process
do_accept(LSocket) ->
    {ok, Socket} = gen_tcp:accept(LSocket),
    spawn_link(module, do_echo, [Socket]),
    do_accept(LSocket).

%% Waiting for usual data, or signal to stop server
do_echo(Socket) ->
    case gen_tcp:recv(Socket, 0) of
		% close server
        {ok, "exit"} ->
			stop();
		% usual data
        {ok, Data} ->
            gen_tcp:send(Socket, Data),
            do_echo(Socket);
        {error, closed} ->
            ok
    end.

