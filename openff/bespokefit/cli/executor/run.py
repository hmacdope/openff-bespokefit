from typing import Optional

import click
import click.exceptions
import rich
from rich import pretty
from rich.padding import Padding

from openff.bespokefit.cli.executor.launch import launch_options
from openff.bespokefit.cli.executor.submit import _submit, submit_options
from openff.bespokefit.cli.utilities import create_command, print_header
from openff.bespokefit.executor.utilities import handle_common_errors


def _run_cli(
    input_file_path: Optional[str],
    molecule_smiles: Optional[str],
    output_file_path: str,
    force_field_path: Optional[str],
    spec_name: Optional[str],
    spec_file_name: Optional[str],
    directory: str,
    n_fragmenter_workers: int,
    n_qc_compute_workers: int,
    n_optimizer_workers: int,
    launch_redis_if_unavailable: bool,
):
    """Run bespoke optimization using a temporary executor.

    If you are running many bespoke optimizations it is recommended that you first launch
    a bespoke executor using the `launch` command and then submit the optimizations to it
    using the `submit` command.
    """

    pretty.install()

    console = rich.get_console()
    print_header(console)

    from openff.bespokefit.executor import BespokeExecutor, wait_until_complete

    executor_status = console.status("launching the bespoke executor")
    executor_status.start()

    with BespokeExecutor(
        directory=directory,
        n_fragmenter_workers=n_fragmenter_workers,
        n_qc_compute_workers=n_qc_compute_workers,
        n_optimizer_workers=n_optimizer_workers,
        launch_redis_if_unavailable=launch_redis_if_unavailable,
    ):

        executor_status.stop()
        console.print("[[green]✓[/green]] bespoke executor launched")
        console.line()

        with handle_common_errors(console) as error_state:

            response_id = _submit(
                console=console,
                input_file_path=input_file_path,
                molecule_smiles=molecule_smiles,
                force_field_path=force_field_path,
                spec_name=spec_name,
                spec_file_name=spec_file_name,
            )

            console.print(Padding("3. running the fitting pipeline", (1, 0, 1, 0)))

            results = wait_until_complete(response_id)

            console.print(
                Padding(
                    f"outputs have been saved to "
                    f"[repr.filename]{output_file_path}[/repr.filename]",
                    (1, 0, 1, 0),
                )
            )

            with open(output_file_path, "w") as file:
                file.write(results.json())

        if error_state["has_errored"]:
            raise click.exceptions.Exit(code=2)


__run_options = [*submit_options()]
__run_options.insert(
    1,
    click.option(
        "--output",
        "output_file_path",
        type=click.Path(exists=False, file_okay=True, dir_okay=False),
        help="The JSON file to save the results to",
        default="output.json",
        show_default=True,
    ),
)
__run_options.extend(launch_options())

run_cli = create_command(
    click_command=click.command("run"), click_options=__run_options, func=_run_cli
)
