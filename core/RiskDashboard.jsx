const PortfolioLiquidationMap = ({ positions }) => {
  const [heatmapData, setHeatmapData] = useState([]);

  useEffect(() => {
    const riskData = positions.map(pos => ({
      x: pos.platform,
      y: pos.healthFactor,
      value: pos.liquidationRiskScore
    }));
    setHeatmapData(riskData);
  }, [positions]);

  return (
    <Heatmap 
      data={heatmapData}
      xLabel="Trading platform"
      yLabel="Health Factor"
    />
  )
}
