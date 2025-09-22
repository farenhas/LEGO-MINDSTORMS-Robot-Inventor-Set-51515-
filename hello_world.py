import hub
import runtime
import sys
import system

async def run(vm, stack):
    vm.broadcast("run")

async def display(vm, stack):
    await vm.system.display.write_async("Hello world")

async def sound(vm, stack):
    await vm.system.sound.play_async("/extra_files/Hello")
    await vm.system.sound.play_async("/extra_files/Celebrate")

async def cancel(vm, stack):
    vm.stop_stacks(except_stack=stack)
    hub.display.clear()
    hub.sound.beep(0, 0)

def setup(rpc, system, stop):
    vm = runtime.VirtualMachine(rpc, system, stop, "hello_world")
    vm.register_on_start("run_on_start", run)
    vm.register_on_broadcast("display_on_run", display, "run")
    vm.register_on_broadcast("sound_on_run", sound, "run")
    vm.register_on_button("cancel_on_left_button", cancel, "left", "pressed")
    vm.register_on_button("run_on_right_button", run, "right", "pressed")
    return vm

setup(None, system.system, sys.exit).start()
