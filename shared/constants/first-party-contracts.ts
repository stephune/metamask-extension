import { Hex } from '@metamask/utils';
import { CHAIN_IDS } from './network';

// TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
// eslint-disable-next-line @typescript-eslint/naming-convention
export enum EXPERIENCES_TYPE {
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_VALIDATOR_STAKING = 'MetaMask Validator Staking',
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_POOLED_STAKING = 'MetaMask Pooled Staking',
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_THIRD_PARTY_STAKING = 'MetaMask Third Party Staking',
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_POOLED_STAKING_V1 = 'MetaMask Pool Staking (v1)',
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_BRIDGE = 'MetaMask Bridge',
  // TODO: Fix in https://github.com/MetaMask/metamask-extension/issues/31860
  // eslint-disable-next-line @typescript-eslint/naming-convention
  METAMASK_SWAPS = 'MetaMask Swaps',
}

/**
 * A map of first-party contract names to their addresses on various chains.
 */
export const FIRST_PARTY_CONTRACT_NAMES: Record<
  EXPERIENCES_TYPE,
  Record<Hex, Hex>
> = {
  [EXPERIENCES_TYPE.METAMASK_VALIDATOR_STAKING]: {
    [CHAIN_IDS.MAINNET]: '0xDc71aFFC862fceB6aD32BE58E098423A7727bEbd',
  },
  [EXPERIENCES_TYPE.METAMASK_POOLED_STAKING]: {
    [CHAIN_IDS.MAINNET]: '0x4FEF9D741011476750A243aC70b9789a63dd47Df',
  },
  [EXPERIENCES_TYPE.METAMASK_THIRD_PARTY_STAKING]: {
    [CHAIN_IDS.MAINNET]: '0x1f6692E78dDE07FF8da75769B6d7c716215bC7D0',
  },
  [EXPERIENCES_TYPE.METAMASK_POOLED_STAKING_V1]: {
    [CHAIN_IDS.MAINNET]: '0xc7bE520a13dC023A1b34C03F4Abdab8A43653F7B',
  },
  [EXPERIENCES_TYPE.METAMASK_BRIDGE]: {
    [CHAIN_IDS.MAINNET]: '0x0439e60F02a8900a951603950d8D4527f400C3f1',
    [CHAIN_IDS.OPTIMISM]: '0xB90357f2b86dbfD59c3502215d4060f71DF8ca0e',
    [CHAIN_IDS.BSC]: '0xaEc23140408534b378bf5832defc426dF8604B59',
    [CHAIN_IDS.POLYGON]: '0x3A0b42cE6166abB05d30DdF12E726c95a83D7a16',
    [CHAIN_IDS.ZKSYNC_ERA]: '0x357B5935482AD8a4A2e181e0132aBd1882E16520',
    [CHAIN_IDS.BASE]: '0xa20ECbC821fB54064aa7B5C6aC81173b8b34Df71',
    [CHAIN_IDS.ARBITRUM]: '0x23981fC34e69eeDFE2BD9a0a9fCb0719Fe09DbFC',
    [CHAIN_IDS.AVALANCHE]: '0x29106d08382d3c73bF477A94333C61Db1142E1B6',
    [CHAIN_IDS.LINEA_MAINNET]: '0xE3d0d2607182Af5B24f5C3C2E4990A053aDd64e3',
  },
  [EXPERIENCES_TYPE.METAMASK_SWAPS]: {
    [CHAIN_IDS.MAINNET]: '0x881D40237659C251811CEC9c364ef91dC08D300C',
    [CHAIN_IDS.BSC]: '0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31',
    [CHAIN_IDS.POLYGON]: '0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31',
    [CHAIN_IDS.AVALANCHE]: '0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31',
    [CHAIN_IDS.ARBITRUM]: '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6',
    [CHAIN_IDS.OPTIMISM]: '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6',
    [CHAIN_IDS.ZKSYNC_ERA]: '0xf504c1fe13d14DF615E66dcd0ABF39e60c697f34',
    [CHAIN_IDS.LINEA_MAINNET]: '0x9dDA6Ef3D919c9bC8885D5560999A3640431e8e6',
  },
};
