class LossHarvester:
    def execute_tax_loss(self, position):
        if position.unrealized_loss > 1000:  # $1000 threshold
            if not self.wash_sale_check(position.asset):
                self.exchange.sell(position.asset, position.amount)
                self.schedule_rebuy(position.asset)
