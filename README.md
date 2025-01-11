AI Application: Thompson Sampling for Multi-Armed Bandit Problem 🎰

This project implements the Thompson Sampling algorithm to solve a multi-armed bandit problem, simulating the process of selecting the best strategy (or "slot machine") based on conversion rates. The goal is to maximize rewards by dynamically choosing the best-performing strategy using probability distributions.
Purpose

The primary goal of this project is to:

    Simulate an environment where multiple strategies with different conversion rates compete.
    Compare random selection with Thompson Sampling to identify which strategy yields the best results.
    Demonstrate how AI can be used for decision-making in uncertain environments with incomplete information.

Methodology

    Environment Setup:
        Nine different strategies (or "slot machines") are defined with varying conversion rates.
        A simulation of 10,000 rounds is performed, where each strategy either succeeds or fails based on its conversion rate.

    Algorithms Implemented:
        Random Selection: Selects a strategy randomly at each round.
        Thompson Sampling: Uses the beta distribution to probabilistically choose the strategy with the highest likelihood of success, updating based on wins and losses.

    Reward Calculation:
        Rewards are accumulated for both random selection and Thompson Sampling.
        The relative return is calculated to measure the performance improvement of Thompson Sampling over random selection.

Key Results

    The algorithm identifies the strategy with the highest conversion rate as the best-performing option.
    The relative return indicates how much more effective Thompson Sampling is compared to random selection.
    A histogram of strategy selections is plotted to visualize the frequency of each strategy being chosen by Thompson Sampling.
