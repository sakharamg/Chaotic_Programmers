factorial:= factorial.cpp
functions:= functions.h
hello:= hello.cpp
main:= main.cpp
output:= hello
objects := $(factorial:%.cpp=%.o) $(hello:%.cpp=%.o) $(main:%.cpp=%.o)
CFLAGS:=-c
OUTFLAG:= -o

all: $(output) 

$(output): $(objects)
	g++ $^ $(OUTFLAG) $@

$(factorial:%.cpp=%.o): $(factorial) $(functions)
$(hello:%.cpp=%.o): $(hello) $(functions)
$(main:%.cpp=%.o): $(main) $(functions)
	g++ $(CFLAGS) $(OUTFLAG) $@ $<

.PHONY : clean all run

.SILENT : clean

clean: RMFLAG:= -rf
clean:
	rm $(RMFLAG) $(objects) $(output)

run:	$(output)
	./$<

