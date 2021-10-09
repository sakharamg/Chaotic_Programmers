output:= ../client
utils:= cl_utils.o
task:= cl_task.o
client:= mt_client.o
path_folder := ./build/
port:=8088
objects := $(utils) $(task) $(client)
CC:=gcc
OUTFLAG:= -o
CFLAGS:=-c -Wall $(OUTFLAG)
MKFLAG:= -p

RM:= rm
MKDIR:= mkdir


all: $(output)

$(output): EXTRAFLAG:= -pthread -g
$(output): $(objects:%.o=$(path_folder)%.o)
	$(CC) $(EXTRAFLAG) $^ $(OUTFLAG) $@

$(utils:%.o=$(path_folder)%.o): $(utils:%.o=%.c) $(utils:%.o=%.h)
	$(MKDIR) $(MKFLAG) $(dir $@)
	$(CC) $(CFLAGS) $@ $<
	
$(task:%.o=$(path_folder)%.o): $(task:%.o=%.c) $(task:%.o=%.h)
	$(MKDIR) $(MKFLAG) $(dir $@)
	$(CC) $(CFLAGS) $@ $<
	
$(client:%.o=$(path_folder)%.o): $(client:%.o=%.c) $(utils:%.o=%.h) $(task:%.o=%.h)
	$(MKDIR) $(MKFLAG) $(dir $@)
	$(CC) $(CFLAGS) $@ $<

.PHONY : clean all run

.SILENT : clean

clean: RMFLAG:= -rf
clean:
	$(RM) $(RMFLAG) $(path_folder) $(output)

all: EXTRAFLAG:= -pthread -g

run: out_param:= localhost $(port)
run:	$(output)
	./$< $(out_param) $(NTHREADS)

