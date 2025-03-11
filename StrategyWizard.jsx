import { useWeb3React } from '@web3-react/core'

const LiquidationsShield = ({ positions }) => {
  const { account } = useWeb3React();

  return (
    <div>
      <h3>Ликвидационная защита</h3>
      {positions.map(pos => (
        <PositionMonitor 
          key={pos.id}
          healthFactor={pos.healthFactor}
          threshold={pos.threshold}
        />
      ))}
    </div>
  )
}
