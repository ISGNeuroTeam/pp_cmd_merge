import pandas as pd
from otlang.sdk.syntax import Keyword, Positional, OTLType, Subsearch
from pp_exec_env.base_command import BaseCommand, Syntax


class PdMergeCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Subsearch("right", required=True),
            Keyword("how", required=False, otl_type=OTLType.TEXT),
            Keyword("on", required=True, otl_type=OTLType.STRING),
            Keyword("copy", otl_type=OTLType.BOOLEAN, required=False),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        self.log_progress('Start pd_merge command')
        # that is how you get arguments
        right_df = self.get_arg("right").value
        how = self.get_arg('how').value
        if how is None:
            how = 'inner'
        on = self.get_arg('on').value.split(',')
        copy = self.get_arg('copy').value
        if copy is None:
            copy = True

        return df.merge(right_df, how=how, on=on, copy=copy)
