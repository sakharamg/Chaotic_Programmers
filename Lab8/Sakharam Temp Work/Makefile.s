output:= ../server
utils:= sv_utils.o
task:= sv_task.o
client:= mt_server.o
path_folder := ./build/

objects := $(utils) $(task) $(client)

OUTFLAG:= -o
CFLAGS:=-c -Wextra $(OUTFLAG)
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

run: port:=8089
run:	$(output)
	./$< $(port)

