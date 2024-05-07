import omni.ext
import omni.ui as ui

# 05/07 use the command in the Extension 
import omni.kit.commands

# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[victor.hello.world] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class VictorHelloWorldExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[victor.hello.world] victor hello world startup")

        self._count = 0

        self._window = ui.Window("Spawn Primitives", width=300, height=300)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("")


                def on_click(prim_type):
                    self._count += 1
                    label.text = f"count: {self._count}"
                    #Create a Cube
                    omni.kit.commands.execute('CreateMeshPrimWithDefaultXform',
                        prim_type=prim_type)

                def on_reset():
                    self._count = 0
                    label.text = "empty"

                on_reset()

                with ui.HStack():
                    ui.Button("Spawn Cube", clicked_fn=lambda: on_click('Cube'))
                    ui.Button("Spawn Cone", clicked_fn=lambda: on_click('Cone'))
                    ui.Button("Spawn Disk", clicked_fn=lambda: on_click('Disk'))
                
                ui.Button("Reset", clicked_fn=on_reset)

    def on_shutdown(self):
        print("[victor.hello.world] victor hello world shutdown")
