from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start'
        self.RestartCommand = f'restart'
        self.StatsCommand = f'stats'
        self.LogCommand = f'log'
        self.PingCommand = f'ping'
        self.StatusCommand = f'status'
        self.MirrorCommand = f'mirror{CMD_INDEX}'
        self.UnzipMirrorCommand = f'unzip{CMD_INDEX}'
        self.ZipMirrorCommand = f'zip{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.HelpCommand = f'help{CMD_INDEX}'
        self.CloneCommand = f'clone{CMD_INDEX}'
        self.CountCommand = f'count{CMD_INDEX}'
        self.WatchCommand = f'watch{CMD_INDEX}'
        self.ZipWatchCommand = f'zipwatch{CMD_INDEX}'
        self.QbMirrorCommand = f'qb{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'qbunzip{CMD_INDEX}'
        self.QbZipMirrorCommand = f'qbzip{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leech{CMD_INDEX}'
        self.UnzipLeechCommand = f'unzipleech{CMD_INDEX}'
        self.ZipLeechCommand = f'zipleech{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbunzipleech{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbzipleech{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch{CMD_INDEX}'
        self.BtSelectCommand = f'btsel{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssSettingsCommand = f'rssset{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_INDEX}'
        self.SleepCommand = f'sleep{CMD_INDEX}'

BotCommands = _BotCommands()
