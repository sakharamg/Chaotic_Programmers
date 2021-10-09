CD:= cd
CDFLAG:= -s
NTHREADS=2
CLIENT_PATH:=./mt_client/
SERVER_PATH:=./mt_server/
export NTHREADS

.SILENT: clean
.PHONY: all clean run-server run-client

all:
	$(CD) $(SERVER_PATH);$(MAKE) $(CDFLAG) all
	$(CD) $(CLIENT_PATH);$(MAKE) $(CDFLAG) all

clean:
	$(CD) $(SERVER_PATH);$(MAKE) $(CDFLAG) clean
	$(CD) $(CLIENT_PATH);$(MAKE) $(CDFLAG) clean

run-server:
	$(CD) $(SERVER_PATH);$(MAKE) $(CDFLAG) run

run-client:
	$(CD) $(CLIENT_PATH);$(MAKE) $(CDFLAG) run
