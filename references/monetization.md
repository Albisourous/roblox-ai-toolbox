Read when: designing a store, setting purchase flows, or reviewing Roblox monetization.

# Roblox AI toolbox: Monetization

## Choose a fair model

For competitive games and games with leaderboards, sell appearance and expression. Paid items must not change movement, hitboxes, score, or access to a fair result. Avoid paid revives and continues when failure is part of the challenge. They can weaken trust and make a leaderboard less credible.

Avoid paid random boxes. Roblox may require odds disclosures, and randomized purchases can prompt parent complaints. Check current rules before designing any random paid reward: https://create.roblox.com/docs/production/monetization

Do not use fake countdowns, invented social proof, or urgency that has no real end. Do not rotate Robux items to create fear of missing out. A scheduled release can organize a catalog, but players must not be misled about availability.

## Build a clear catalog

- Offer a low-cost first purchase for younger players and families. Keep some customization earnable so new players can express themselves before buying.
- Use outfit or bundle passes for complete looks. A pass is a permanent-unlock primitive, so describe exactly what it grants.
- Set a price ladder by value. Entry items should feel attainable, while larger bundles should provide a coherent set rather than arbitrary item count.
- Make paid value consistent. Larger soft-currency packs should grant more currency per Robux than smaller packs.
- Calculate value tags from actual pack grants and current prices. Do not invent a currency exchange rate to make one offer look cheaper.
- A one-time first top-up bonus can help a first buyer understand the currency. Label it clearly and grant it once.
- Feature a small selection of discounted items in soft currency. Calculate discounts from the catalog price on the server and use the same rule for every purchase path.
- Hide unreleased catalog entries completely. Do not show empty placeholders or "SOON" teasers.

One shipped runner used R$79/149/249/399 as an example pass ladder. This is a labeled product example, not a Roblox price recommendation or platform fact.

Show owned looks in a lobby, player card, or board so the store can be discovered through play. Do not open purchase prompts during a run. Ask players to choose a product before showing the Roblox purchase dialog.

## Show a trustworthy price

Fetch the current displayed price with `MarketplaceService:GetProductInfoAsync` and use configured price data only as a fallback. A fallback is not proof of a player's personalized or regional quote. Label it as a configured estimate or wait until a definite quote is available. Verify current API behavior and pricing rules in Creator Docs: https://create.roblox.com/docs/reference/engine/classes/MarketplaceService

Managed or regional pricing may require a one-time Creator Dashboard opt-in before API changes succeed. Observed: a price toggle before opt-in returned `InvalidManagedPricing`. Treat this as an operational check, not a guaranteed error message. Verify current Creator Docs and Dashboard settings before changing prices.

## Protect purchase grants

In `MarketplaceService.ProcessReceipt`, grant developer products through durable, idempotent receipt handling. Store each `PurchaseId` in the player's persistent profile with the grant. If Roblox retries a receipt, the profile must prevent a second grant. Verify the current callback contract in Creator Docs: https://create.roblox.com/docs/reference/engine/classes/MarketplaceService

- Return `NotProcessedYet` until the player's profile has loaded.
- If profile loading fails, block all purchase-related profile writes. Do not acknowledge a receipt that cannot be saved.
- Keep the receipt id and grant in one durable update where possible. Retry safely after transient storage errors.
- Test receipt redelivery, rejoin, and failed profile loading before release.

For passes, derive ownership from `UserOwnsGamePassAsync` and cache the result for the session. Use that as the source of truth rather than a client-supplied flag. The server must revalidate every equip request against current ownership and the allowed catalog.

Publish the matching grant code before changing a developer-product price. Otherwise a player can buy at the new price while the live grant still uses old assumptions.

Before publishing, verify the new-player store view with a debug ownership mask. The list must be empty in the release build. The creator account can own every test pass, which can hide broken first-purchase views.

## Stock the store for every spender at launch

Launch with products for every spender level, not only the entry tier. In one observed launch, limited-run items added two weeks late still became a top seller, and the creator counted the delay as lost revenue. For progression games, repeat-purchase consumables and a ladder of cheap upgrade tiers drive volume: a first tier priced at a few Robux moves a player across the player-to-payer threshold, and later tiers stack on it. This is the same loss-leader pattern retail stores use.

Make scarcity real. A limited item needs a fixed stock that is never restocked. Match at least one limited to your largest demographic segment - check the audience split in Creator Hub analytics before choosing what to offer. Scarcity can also serve balance: a limited, high-priced version of a powerful item sells while keeping it rare.

Protect the economy from your own store. In that launch the creator blamed raw currency packs and overpowered event handouts for breaking the sinks the economy depended on. Prefer scarce, expensive versions of strong items over unlimited cheap power, and apply the same discipline to free handouts during live events.

Check the store on a phone before launch. In the same launch, fixing the mobile shop layout measurably recovered revenue per daily active user.

## Review the full path

For each product, document the display name, grant, price source, receipt behavior, and refund or recovery path. Check the purchase prompt on a non-owner account. Confirm the product displays a definite quote, the server grants once, the balance persists, and a rejoin preserves ownership.

Keep purchase analytics separate from a financial ledger. Compare receipts with durable profile state and Creator Hub reports. Use dry runs for scripts that touch live listings, and require an explicit apply flag before writes.
